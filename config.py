import os
from typing import Any, Dict

class Config:
    DEFAULTS = {
        "NETWORK": "mainnet",
        "RPC_URL": "https://api.mainnet.node",
        "TIMEOUT": 30,
        "DEBUG": False
    }

    def __init__(self, env_prefix: str = "WALLET_"):
        self.env_prefix = env_prefix
        self._config = self.DEFAULTS.copy()
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key in self.DEFAULTS:
            env_key = f"{self.env_prefix}{key}"
            value = os.getenv(env_key)
            if value is not None:
                self._config[key] = self._coerce_type(key, value)

    def _coerce_type(self, key: str, value: str) -> Any:
        default_val = self.DEFAULTS[key]
        if isinstance(default_val, bool):
            return value.lower() in ("true", "1", "yes")
        if isinstance(default_val, int):
            return int(value)
        return value

    def get(self, key: str) -> Any:
        return self._config.get(key)

def get_config() -> Config:
    return Config()