import os
import subprocess
from typing import Any

from statusbar_hid_battery_info.device import Device


class Util:
    @staticmethod
    def extract_battery_info(input_data: str, device_name: str) -> int | None:
        find_battery_level: bool = False
        for line in input_data.split("\n"):
            if "\"Product\"" in line and device_name in line:
                find_battery_level = True
            if find_battery_level and "BatteryPercent" in line:
                battery_percent: int = int(line.split("=")[1].strip(" "))
                return battery_percent
        return None

    @staticmethod
    def detect_devices(input_data: str) -> list[Device]:
        device_count: int = 0
        raw_devices: list[dict[str, Any]] = []
        for line in input_data.split("\n"):
            if line.startswith("+-o AppleDeviceManagementHIDEventService"):
                device_count += 1
                raw_devices.append({})
            if "\"HasBattery\"" in line:
                raw_devices[device_count - 1]["has_battery"] = True if "Yes" in line else False
            if "\"DeviceAddress\"" in line:
                raw_devices[device_count - 1]["device_address"] = line.split("=")[1].strip(" \"")
            if "\"VendorID\"" in line:
                raw_devices[device_count - 1]["vendor_id"] = int(line.split("=")[1].strip(" \""))
            if "\"ProductID\"" in line:
                raw_devices[device_count - 1]["product_id"] = int(line.split("=")[1].strip(" \""))
            if "\"Transport\"" in line:
                raw_devices[device_count - 1]["is_bluetooth"] = True if "Bluetooth" in line else False
            if "\"Product\"" in line:
                raw_devices[device_count - 1]["product_name"] = line.split("=")[1].strip(" \"")

        devices: list[Device] = [Device(**raw_device) for raw_device in raw_devices]

        return devices

    @staticmethod
    def get_device_info_from_os() -> str:
        command: str = "ioreg -c AppleDeviceManagementHIDEventService -r -l"
        output = subprocess.check_output(command.split(" ")).decode("utf-8")

        return output

    @staticmethod
    def send_notification(title: str, subtitle: str, message: str):
        os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\" subtitle \"{subtitle}\"'")
