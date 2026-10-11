from typing import Final, Dict, List

# Crypto currency network constants
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

NETWORKS: Final[Dict[str, str]] = {
    "mainnet": "https://mainnet.infura.io/v3/",
    "sepolia": "https://sepolia.infura.io/v3/",
    "polygon": "https://polygon-rpc.com"
}

SUPPORTED_TOKENS: Final[List[str]] = ["ETH", "BTC", "USDT", "USDC"]

MIN_GAS_LIMIT: Final[int] = 21000
DEFAULT_DECIMALS: Final[int] = 18

def get_network_url(name: str) -> str:
    """Return the RPC URL for a given network name."""
    return NETWORKS.get(name, NETWORKS["mainnet"])

class ConfigDefaults:
    """Configuration default values for wallet operations."""
    BATCH_SIZE: int = 10
    DEBUG_MODE: bool = False
    LOG_FILE: str = "wallet.log"