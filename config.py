import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.settings = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    user_data = json.load(f)
                    self.settings.update(user_data)
                except json.JSONDecodeError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

config = ConfigLoader()