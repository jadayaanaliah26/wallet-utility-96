import os
from typing import Dict, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkConfig:
    mainnet: str = "https://mainnet.infura.io/v3/"
    testnet: str = "https://sepolia.infura.io/v3/"

class Settings:
    def __init__(self) -> None:
        self._env: str = os.getenv("ENV", "development")
        self.timeout: int = 30
        self.retry_limit: int = 3

    @property
    def network_urls(self) -> Dict[str, str]:
        return {
            "prod": NetworkConfig.mainnet,
            "dev": NetworkConfig.testnet
        }

    def get_provider_url(self) -> str:
        key = "prod" if self._env == "production" else "dev"
        return self.network_urls[key] + os.getenv("API_KEY", "")

config = Settings()