import logging
import sys
from distutils.version import LooseVersion
from importlib import metadata
from pathlib import Path
from typing import Any
from typing import Final

import requests
import orjson as json

BINARY_NAME: Final[str] = "StatusbarHIDBattInfo"
GITHUB_URL: Final[str] = "https://api.github.com/repos/derfryday/statusbar_hid_battery_info/releases/latest"


class Updater:
    @staticmethod
    def update() -> None:
        local_binary_path: Path = Path(sys.argv[0]).resolve()
        assets: list[dict[str, Any]] = Updater.get_latest_version_info_from_github()["assets"]

        if len(assets) == 0:
            raise Exception("No assets found for latest release!")

        new_binary_url: str = \
            [asset["browser_download_url"] for asset in assets if asset["name"] == BINARY_NAME][0]
        logging.info("Found new binary at url: %s", new_binary_url)

        response = requests.get(url=new_binary_url)
        if response.status_code == 200:
            logging.info("Downloading update and replacing binary...")
            local_binary_path.write_bytes(response.content)
        else:
            raise Exception("Could not download update!")

    @staticmethod
    def get_latest_version_info_from_github() -> dict[str, Any]:
        url: str = GITHUB_URL
        response = requests.get(url=url)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("Could not get latest version info from github!")

    @staticmethod
    def get_latest_version() -> LooseVersion:
        latest_version: LooseVersion = Updater.get_latest_version_info_from_github()["tag_name"]
        logging.info("Latest version: %s", latest_version)
        return latest_version

    @staticmethod
    def update_available() -> bool:
        latest_version: LooseVersion = Updater.get_latest_version()
        current_version: LooseVersion = LooseVersion(metadata.version(__package__ or __name__))

        return latest_version > current_version
