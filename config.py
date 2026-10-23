import os
from typing import Dict, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkConfig:
    mainnet_rpc: str = "https://mainnet.infura.io/v3/"
    testnet_rpc: str = "https://sepolia.infura.io/v3/"
    timeout: int = 30

class AppConfig:
    def __init__(self) -> None:
        self._config: Dict[str, Any] = {
            "environment": os.getenv("ENV", "production"),
            "retry_limit": int(os.getenv("RETRY_LIMIT", "3")),
            "log_level": os.getenv("LOG_LEVEL", "INFO")
        }

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def network(self) -> NetworkConfig:
        return NetworkConfig()

def load_config() -> AppConfig:
    return AppConfig()