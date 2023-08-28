import logging
import sys
from argparse import ArgumentParser
from pathlib import Path

from statusbar_hid_battery_info import StatusbarHIDBattInfo
from statusbar_hid_battery_info.config import ConfigFile
from statusbar_hid_battery_info.agent import LaunchAgent
from statusbar_hid_battery_info.device import Device
from statusbar_hid_battery_info.util import Util


def main() -> None:
    parser = ArgumentParser(description="Statusbar Time Tracker command line interface")
    parser.add_argument("--setup", dest="run_setup", action="store_true", default=False)
    parser.add_argument("--install", dest="install", action="store_true", default=False)
    parser.add_argument("--uninstall", dest="uninstall", action="store_true", default=False)
    parser.add_argument("--configure", dest="configure", action="store_true", default=False)
    parser.add_argument("--log-level", dest="log_level", choices=["debug", "info", "warning", "error"], default="info")

    args = parser.parse_args()

    log_file: Path = Path.home() / "Library/Logs/StatusbarHIDBattInfo.log"

    logging.basicConfig(filename=str(log_file), level=getattr(logging, args.log_level.upper()))
    logging.getLogger().addHandler(logging.StreamHandler())
    config_path = Path.home() / ".config/statusbar_hid_batt_info.json"

    if args.run_setup:
        logging.info("Creating default config...")
        ConfigFile.create_default_config()
        sys.exit(0)
    elif args.install:
        logging.info("Installing StatusbarHIDBattInfo...")
        LaunchAgent.create_launchd_file()
        LaunchAgent.enable_launchd_service()
        LaunchAgent.start_launchd_agent()
        sys.exit(0)
    elif args.uninstall:
        logging.info("Uninstalling StatusbarHIDBattInfo...")
        LaunchAgent.disable_launchd_service()
        LaunchAgent.delete_launchd_file()
        sys.exit(0)
    elif args.configure:
        ConfigFile.create_default_config()
        sys.exit(0)

    if not config_path.exists():
        logging.error("Config file does not exist, please run setup or configuration wizard!")
        sys.exit(1)
    else:
        devices: list[Device] = [
            device for device in Util.detect_devices(input_data=Util.get_device_info_from_os()) if device.is_bluetooth
        ]
        logging.info(f"Detected {len(devices)} devices: {devices}")
        app: StatusbarHIDBattInfo = StatusbarHIDBattInfo(config_path=config_path, devices=devices)
        logging.info("Starting StatusbarHIDBattInfo...")
        app.run()


if __name__ == "__main__":
    main()
