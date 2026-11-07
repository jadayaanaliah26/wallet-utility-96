import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.15,
    "enable_cache": True,
    "cache_ttl": 300,
}


@dataclass
class AppConfig:
    network: str = DEFAULT_CONFIG["network"]
    rpc_url: str = DEFAULT_CONFIG["rpc_url"]
    request_timeout: int = DEFAULT_CONFIG["request_timeout"]
    max_retries: int = DEFAULT_CONFIG["max_retries"]
    gas_limit_multiplier: float = DEFAULT_CONFIG["gas_limit_multiplier"]
    enable_cache: bool = DEFAULT_CONFIG["enable_cache"]
    cache_ttl: int = DEFAULT_CONFIG["cache_ttl"]

    @classmethod
    def load(cls, path: Optional[str] = None) -> "AppConfig":
        merged = DEFAULT_CONFIG.copy()

        if path and Path(path).is_file():
            with open(path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                merged.update(file_data)

        env_rpc = os.getenv("WALLET_RPC_URL")
        if env_rpc:
            merged["rpc_url"] = env_rpc

        env_network = os.getenv("WALLET_NETWORK")
        if env_network:
            merged["network"] = env_network

        return cls(
            network=str(merged["network"]),
            rpc_url=str(merged["rpc_url"]),
            request_timeout=int(merged["request_timeout"]),
            max_retries=int(merged["max_retries"]),
            gas_limit_multiplier=float(merged["gas_limit_multiplier"]),
            enable_cache=bool(merged["enable_cache"]),
            cache_ttl=int(merged["cache_ttl"]),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
