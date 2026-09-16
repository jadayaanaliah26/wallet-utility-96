import os
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "chain_id": 1,
    "gas_limit_multiplier": 1.2,
    "request_timeout": 30,
    "max_retries": 3,
    "cache_enabled": True,
}


@dataclass
class Config:
    network: str = DEFAULT_CONFIG["network"]
    rpc_url: str = DEFAULT_CONFIG["rpc_url"]
    chain_id: int = DEFAULT_CONFIG["chain_id"]
    gas_limit_multiplier: float = DEFAULT_CONFIG["gas_limit_multiplier"]
    request_timeout: int = DEFAULT_CONFIG["request_timeout"]
    max_retries: int = DEFAULT_CONFIG["max_retries"]
    cache_enabled: bool = DEFAULT_CONFIG["cache_enabled"]

    @classmethod
    def load(cls, config_path: Optional[Path] = None) -> "Config":
        data = dict(DEFAULT_CONFIG)

        if config_path and config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                data.update({k: v for k, v in file_data.items() if k in DEFAULT_CONFIG})

        env_mappings = {
            "WALLET_NETWORK": ("network", str),
            "WALLET_RPC_URL": ("rpc_url", str),
            "WALLET_CHAIN_ID": ("chain_id", int),
            "WALLET_GAS_MULTIPLIER": ("gas_limit_multiplier", float),
            "WALLET_TIMEOUT": ("request_timeout", int),
            "WALLET_MAX_RETRIES": ("max_retries", int),
        }

        for env_var, (key, type_cast) in env_mappings.items():
            if val := os.getenv(env_var):
                try:
                    data[key] = type_cast(val)
                except ValueError:
                    pass

        return cls(**data)
