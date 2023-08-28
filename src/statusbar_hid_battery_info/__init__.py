import logging
import os
from datetime import datetime
from datetime import timedelta
from importlib.metadata import version
from pathlib import Path

from rumps import App
from rumps import MenuItem
from rumps import timer

from statusbar_hid_battery_info.agent import LaunchAgent
from statusbar_hid_battery_info.config import ConfigFile
from statusbar_hid_battery_info.device import Device
from statusbar_hid_battery_info.updater import Updater
from statusbar_hid_battery_info.util import Util


class StatusbarHIDBattInfo(App):
    def __init__(self, config_path: Path, devices: list[Device]) -> None:
        super(StatusbarHIDBattInfo, self).__init__("Statusbar HID Battery Info", quit_button=MenuItem("Quit", key="q"))

        self.config_path: Path = config_path
        self.devices: list[Device] = devices
        self.config: ConfigFile = ConfigFile(self.config_path)
        self.title = "initialising..."

        self.menu = [
            MenuItem("Scan for Devices", callback=self.scan_for_devices),
            ["Settings", [
                MenuItem("Reload Config", callback=self.reload_config),
                MenuItem("Open Config", callback=self.open_config),
                MenuItem("Check for Updates", callback=self.check_for_updates)
                        ],
            ],
            None,
            f"version: {version(__package__ or __name__)}",
            None
        ]
        self.last_notified: datetime | None = None

    @staticmethod
    def check_for_updates(menu_item: MenuItem):
        if menu_item.title == "Check for Updates":
            logging.info("Checking for updates...")
            if Updater.update_available():
                logging.info("Updates found!")
                Util.send_notification(
                    "Statusbar HID Battery Info",
                    "Update",
                    "Updates found. Install updates at Settings>Install Update and Restart"
                )
                menu_item.title = "Install Update and Restart"

            else:
                logging.info("No updates found!")
                Util.send_notification(
                    "Statusbar HID Battery Info",
                    "Update",
                    "No updates found."
                )
        elif menu_item.title == "Install Update and Restart":
            Updater.update()
            LaunchAgent.restart_launchd_agent()

    def reload_config(self, _):
        logging.info("Reloading config...")
        self.config.load_config()

    def open_config(self, _):
        logging.info("Opening config...")
        os.system(f"open {str(self.config_path)}")

    def notify_batt_level(self, hid_device: Device, level: int | None) -> None:
        notify: bool = False
        next_notify: datetime = datetime.now()
        if isinstance(self.last_notified, datetime):
            next_notify = self.last_notified + timedelta(minutes=self.config.notification_interval)

        if isinstance(level, int):
            if level <= self.config.notification_threshold:
                if datetime.now() >= next_notify:
                    notify = True
        if notify:
            Util.send_notification("Battery Warning", hid_device.product_name, message=f"Battery level is at {level}%")
            self.last_notified = datetime.now()

    def update_title(self) -> None:
        title_string: str = "No devices detected"
        if len(self.devices) > 0:
            device_strings: list[str] = []
            for hid_device in self.devices:
                batt_level = Util.extract_battery_info(
                    input_data=Util.get_device_info_from_os(), device_name=hid_device.product_name
                )
                device_strings.append(
                    f"{self.config.display_names.get(hid_device.product_name, hid_device.product_name)}: {batt_level}%"
                )
                self.notify_batt_level(hid_device=hid_device, level=batt_level)
            title_string = " | ".join(device_strings)
        self.title = title_string

    def scan_for_devices(self, _) -> None:
        logging.info("Scanning for devices...")
        self.devices = [
            hid_device for hid_device in Util.detect_devices(
                input_data=Util.get_device_info_from_os()
            ) if hid_device.is_bluetooth
        ]

    @timer(5)
    def update_device_info(self, _):
        self.update_title()
