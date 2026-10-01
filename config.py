import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "debug": False
}

class ConfigLoader:
    def __init__(self, env_prefix: str = "WALLET_"):
        self.env_prefix = env_prefix
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        for key in self.config.keys():
            env_key = f"{self.env_prefix}{key.upper()}"
            val = os.getenv(env_key)
            if val is not None:
                self.config[key] = self._cast_type(key, val)
        return self.config

    def _cast_type(self, key: str, value: str) -> Any:
        target_type = type(DEFAULT_CONFIG.get(key))
        try:
            if target_type is bool:
                return value.lower() in ("true", "1", "yes")
            return target_type(value)
        except (ValueError, TypeError):
            return value