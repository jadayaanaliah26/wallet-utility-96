import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3
}

class ConfigLoader:
    def __init__(self, file_path: str = "config.json"):
        self.file_path = file_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load_file()

    def _load_file(self) -> None:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.settings