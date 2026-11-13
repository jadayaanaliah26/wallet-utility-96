import json
import os
from typing import Any, Dict

class ConfigLoader:
    DEFAULT_CONFIG = {
        "network": "mainnet",
        "retry_attempts": 3,
        "timeout": 30
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self._config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return self.DEFAULT_CONFIG.copy()
        
        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                return {**self.DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG.copy()

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config