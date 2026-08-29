import os
import json
from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class Config:
    network: str = "mainnet"
    rpc_endpoint: str = "https://rpc.mainnet.com"
    wallet_address: str = ""
    private_key: str = ""
    max_gas_price: int = 100
    enable_logging: bool = False

def load_config(path: str = "config.json") -> Config:
    defaults: Dict[str, Any] = {
        "network": "mainnet",
        "rpc_endpoint": "https://rpc.mainnet.com",
        "wallet_address": "",
        "private_key": "",
        "max_gas_price": 100,
        "enable_logging": False,
    }
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            file_data = json.load(f)
            defaults.update({k: v for k, v in file_data.items() if k in defaults})
    env_prefix = "WALLET_"
    env_map = {
        "network": "NETWORK",
        "rpc_endpoint": "RPC_ENDPOINT",
        "wallet_address": "ADDRESS",
        "private_key": "PRIVATE_KEY",
        "max_gas_price": "MAX_GAS_PRICE",
        "enable_logging": "ENABLE_LOGGING",
    }
    for key, env_key in env_map.items():
        env_val = os.getenv(env_prefix + env_key)
        if env_val is not None:
            if key == "max_gas_price":
                defaults[key] = int(env_val)
            elif key == "enable_logging":
                defaults[key] = env_val.lower() in ("true", "1", "yes")
            else:
                defaults[key] = env_val
    return Config(**defaults)

def save_config(config: Config, path: str = "config.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(asdict(config), f, indent=2)
