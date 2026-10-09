import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth.llamarpc.com",
    "timeout": 30,
    "max_fee_per_gas_gwei": 100,
    "cache_dir": "~/.wallet_utility_96/cache"
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass
        for key in config:
            env_key = f"WALLET_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                default_val = config[key]
                if isinstance(default_val, int):
                    config[key] = int(val)
                elif isinstance(default_val, float):
                    config[key] = float(val)
                elif isinstance(default_val, bool):
                    config[key] = val.lower() in ("true", "1", "yes")
                else:
                    config[key] = val
        return config

    def get(self, key: str) -> Any:
        return self.config.get(key)
