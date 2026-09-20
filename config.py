import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "STRICT_MODE": True
}

class ConfigLoader:
    def __init__(self, env_prefix: str = "WALLET_"):
        self.prefix = env_prefix

    def load(self, overrides: Dict[str, Any] = None) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        
        for key in DEFAULT_CONFIG:
            env_val = os.getenv(f"{self.prefix}{key}")
            if env_val is not None:
                config[key] = self._cast_type(key, env_val)
        
        if overrides:
            config.update(overrides)
        return config

    def _cast_type(self, key: str, value: str) -> Any:
        default = DEFAULT_CONFIG[key]
        if isinstance(default, bool):
            return value.lower() in ("true", "1", "yes")
        if isinstance(default, int):
            return int(value)
        return value

def get_config() -> Dict[str, Any]:
    return ConfigLoader().load()