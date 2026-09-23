import os
from typing import Any, Dict

class ConfigLoader:
    DEFAULTS = {
        "NETWORK": "mainnet",
        "RPC_URL": "https://api.mainnet.chain",
        "TIMEOUT": 30,
        "DEBUG": False
    }

    def __init__(self, env_prefix: str = "WALLET_"):
        self.env_prefix = env_prefix
        self.config: Dict[str, Any] = self.DEFAULTS.copy()
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key in self.DEFAULTS:
            env_val = os.getenv(f"{self.env_prefix}{key}")
            if env_val is not None:
                self.config[key] = self._cast_type(key, env_val)

    def _cast_type(self, key: str, value: str) -> Any:
        default = self.DEFAULTS[key]
        if isinstance(default, bool):
            return value.lower() in ("true", "1", "yes")
        if isinstance(default, int):
            return int(value)
        return value

    def get(self, key: str) -> Any:
        return self.config.get(key)

config = ConfigLoader()