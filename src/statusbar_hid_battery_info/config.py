from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import orjson as json


class ConfigFile:
    def __init__(self, config_path: Path) -> None:
        self._file_path: Path = config_path
        self._raw_config: dict[str, Any] = {}

        self.load_config()

    @staticmethod
    def create_default_config(config_path: Path | None = None) -> None:
        if config_path is None:
            config_path = Path.home() / ".config" / "statusbar_hid_batt_info.json"
        default_config: dict[str, Any] = {
            "display_names": {
                "Magic Keyboard with Numeric Keypad": "⌨️",
                "Magic Mouse": "🖱️"
            },
            "notification_settings": {
                "threshold": 20,
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
        return self._raw_config.get("display_names", {})

    @property
    def notification_settings(self) -> dict[str, Any]:
        return self._raw_config.get("notification_settings", {})

    @property
    def notification_threshold(self) -> int:
        return self.notification_settings.get("threshold", 20)

    @property
    def notification_interval(self) -> int:
        return self.notification_settings.get("notification_interval", 60)

    def load_config(self) -> None:
        config = json.loads(self._file_path.read_text(encoding="utf-8"))
        logging.debug("config: %s", config)
        self._raw_config = config

    def write_config(self) -> None:
        self._file_path.write_text(
            json.dumps(self._raw_config, option=json.OPT_INDENT_2).decode("utf-8"), encoding="utf-8"
        )
