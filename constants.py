from typing import Final
from enum import Enum

class ChainID(Enum):
    MAINNET: int = 1
    GOERLI: int = 5
    SEPOLIA: int = 11155111

CACHE_TTL: Final[int] = 300
MAX_RETRIES: Final[int] = 3
DEFAULT_TIMEOUT: Final[float] = 10.0

RPC_ENDPOINTS: Final[dict[ChainID, str]] = {
    ChainID.MAINNET: "https://eth.llamarpc.com",
    ChainID.GOERLI: "https://rpc.ankr.com/eth_goerli",
    ChainID.SEPOLIA: "https://rpc.sepolia.org",
}

BYTE_ORDER: Final[str] = "big"
ADDRESS_LEN: Final[int] = 20
GAS_LIMIT_BUFFER: Final[float] = 1.2

# Performance optimization constants
BATCH_SIZE: Final[int] = 100
CONCURRENCY_LIMIT: Final[int] = 10
PREFETCH_COUNT: Final[int] = 50