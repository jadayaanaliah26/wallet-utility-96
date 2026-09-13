import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "api_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_count": 3,
    "enable_logging": True
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
        return config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)