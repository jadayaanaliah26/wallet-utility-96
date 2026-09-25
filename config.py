import os
from typing import Any, Dict

def get_env(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)

class Config:
    DEFAULT_CONFIG = {
        "RPC_URL": "https://mainnet.infura.io/v3/",
        "CHAIN_ID": 1,
        "TIMEOUT": 30,
        "RETRY_ATTEMPTS": 3
    }

    def __init__(self) -> None:
        self._config = self.DEFAULT_CONFIG.copy()
        self._load_env()

    def _load_env(self) -> None:
        for key in self._config:
            val = os.getenv(key)
            if val is not None:
                self._config[key] = type(self._config[key])(val)

    def get(self, key: str) -> Any:
        return self._config.get(key)

    @property
    def settings(self) -> Dict[str, Any]:
        return self._config.copy()

config = Config()