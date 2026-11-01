import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "rpc_url": "https://api.mainnet.network"
}

def load_config() -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    env_vars = {
        "network": os.getenv("WALLET_NETWORK"),
        "timeout": os.getenv("WALLET_TIMEOUT"),
        "retry_attempts": os.getenv("WALLET_RETRIES"),
        "rpc_url": os.getenv("WALLET_RPC_URL")
    }

    for key, value in env_vars.items():
        if value is not None:
            if isinstance(config[key], int):
                config[key] = int(value)
            else:
                config[key] = value
    return config

settings = load_config()