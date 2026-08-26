import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "NETWORK": "mainnet",
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "GAS_LIMIT": 21000,
    "TIMEOUT_SECONDS": 30,
    "DEBUG_MODE": False,
}


class ConfigLoader:
    def __init__(self, env_prefix: str = "WALLET_") -> None:
        self.env_prefix = env_prefix

    def load(self, overrides: Dict[str, Any] = None) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        
        for key in config:
            env_key = f"{self.env_prefix}{key}"
            if env_key in os.environ:
                val = os.environ[env_key]
                config[key] = self._cast_value(val)

        if overrides:
            config.update(overrides)

        return config

    @staticmethod
    def _cast_value(value: str) -> Any:
        if value.lower() in ("true", "false"):
            return value.lower() == "true"
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            return value
