import os
import json
from dataclasses import dataclass
from typing import Dict, Any, Optional
from pathlib import Path

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "timeout_seconds": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.1,
    "enable_cache": True,
}


@dataclass
class WalletConfig:
    network: str = DEFAULT_CONFIG["network"]
    rpc_url: str = DEFAULT_CONFIG["rpc_url"]
    timeout_seconds: int = DEFAULT_CONFIG["timeout_seconds"]
    max_retries: int = DEFAULT_CONFIG["max_retries"]
    gas_limit_multiplier: float = DEFAULT_CONFIG["gas_limit_multiplier"]
    enable_cache: bool = DEFAULT_CONFIG["enable_cache"]

    @classmethod
    def load(cls, config_path: Optional[str] = None) -> "WalletConfig":
        merged = DEFAULT_CONFIG.copy()

        if config_path and Path(config_path).is_file():
            with open(config_path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                merged.update({k: v for k, v in file_data.items() if k in merged})

        env_mappings = {
            "WALLET_NETWORK": ("network", str),
            "WALLET_RPC_URL": ("rpc_url", str),
            "WALLET_TIMEOUT": ("timeout_seconds", int),
            "WALLET_MAX_RETRIES": ("max_retries", int),
            "WALLET_GAS_MULTIPLIER": ("gas_limit_multiplier", float),
            "WALLET_ENABLE_CACHE": ("enable_cache", lambda v: v.lower() == "true"),
        }

        for env_key, (config_key, caster) in env_mappings.items():
            if env_val := os.getenv(env_key):
                try:
                    merged[config_key] = caster(env_val)
                except ValueError:
                    pass

        return cls(**merged)
