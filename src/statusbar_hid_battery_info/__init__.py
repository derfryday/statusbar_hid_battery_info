import logging
import os
from importlib import metadata
from pathlib import Path

from rumps import App
from rumps import MenuItem
from rumps import timer

from statusbar_hid_battery_info.config import ConfigFile
from statusbar_hid_battery_info.device import Device
from statusbar_hid_battery_info.util import Util


class StatusbarHIDBattInfo(App):
    def __init__(self, config_path: Path, devices: list[Device]) -> None:
        super(StatusbarHIDBattInfo, self).__init__("Statusbar HID Battery Info", quit_button=MenuItem("Quit", key="q"))

        self.config_path: Path = config_path
        self.devices: list[Device] = devices
        self.config: ConfigFile = ConfigFile(self.config_path)
        self.title = "initialising..."

        self.menu = [
            ["Settings", [
                MenuItem("Reload Config", callback=self.reload_config),
                MenuItem("Open Config", callback=self.open_config),
                        ],
            ],
            None,
            f"version: {metadata.version(__package__ or __name__)}",
            None
        ]

    def reload_config(self, _):
        logging.info("Reloading config...")
        self.config.load_config()

    def open_config(self, _):
        logging.info("Opening config...")
        os.system(f"open {str(self.config_path)}")

    def update_title(self) -> None:
        title_string: str = "No devices detected"
        if len(self.devices) > 0:
            device_strings: list[str] = []
            for hid_device in self.devices:
                batt_level: int = 0
                Util.extract_battery_info(
                    input_data=Util.get_device_info_from_os(), device_name=hid_device.product_name
                )
                device_strings.append(
                    f"{self.config.display_names.get(hid_device.product_name, hid_device.product_name)}: {batt_level}%"
                )
            title_string = " | ".join(device_strings)
        self.title = title_string

    def scan_for_devices(self, _) -> None:
        self.devices = [
            hid_device for hid_device in Util.detect_devices(input_data=Util.get_device_info_from_os()) if hid_device.is_bluetooth
        ]

    @timer(5)
    def update_device_info(self, _):
        self.update_title()
