import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "LOG_LEVEL": "INFO"
}

def load_config() -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    env_vars = {
        "RPC_URL": os.getenv("RPC_URL"),
        "TIMEOUT": os.getenv("TIMEOUT"),
        "MAX_RETRIES": os.getenv("MAX_RETRIES"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL")
    }

    for key, value in env_vars.items():
        if value is not None:
            if isinstance(config[key], int):
                config[key] = int(value)
            else:
                config[key] = value
    return config

settings = load_config()