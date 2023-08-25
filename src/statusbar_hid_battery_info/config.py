from pathlib import Path
from typing import Any
from typing import Optional

import orjson as json


class ConfigFile:
    def __init__(self, config_path: Path) -> None:
        self._file_path: Path = config_path
        self._raw_config: dict[str, Any] = {}

    @staticmethod
    def create_default_config(config_path: Optional[Path] = None) -> None:
        if config_path is None:
            config_path = Path.home() / ".config" / "statusbar_hid_battery_info" / "config.json"
        default_config: dict[str, Any] = {
            "display_names": {
                "Apple Internal Keyboard / Trackpad": "⌨️",
                "Magic Mouse": "🖱️"
            },
            "notification_settings": {
                "thresholds": {
                    "warning": 20,
                    "critical": 10,
                },
                "notification_interval": 60,
            }
        }
        config_path.write_text(
            json.dumps(default_config, option=json.OPT_INDENT_2).decode("utf-8"), encoding="utf-8"
        )

    @property
    def config(self) -> dict[str, Any]:
        return self._raw_config

    @property
    def display_names(self) -> dict[str, str]:
        return self._raw_config["display_names"]

    @property
    def notification_settings(self) -> dict[str, Any]:
        return self._raw_config["notification_settings"]

    def load_config(self) -> None:
        self._raw_config = str(json.loads(self._file_path.read_text(encoding="utf-8")))

    def write_config(self) -> None:
        self._file_path.write_text(
            json.dumps(self._raw_config, option=json.OPT_INDENT_2).decode("utf-8"), encoding="utf-8"
        )
