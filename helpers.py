import json
import os
from typing import Any, Dict

class ConfigLoader:
    DEFAULT_CONFIG = {
        "network": "mainnet",
        "rpc_url": "https://api.mainnet-beta.solana.com",
        "timeout": 30,
        "retry_attempts": 3
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return self.DEFAULT_CONFIG
        
        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                return {**self.DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

def load_app_config(path: str = "config.json") -> ConfigLoader:
    return ConfigLoader(path)