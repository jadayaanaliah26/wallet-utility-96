import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "fee_multiplier": 1.2
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.config = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.config.copy()