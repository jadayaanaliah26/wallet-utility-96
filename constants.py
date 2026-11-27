from typing import Final

# Network constants
DEFAULT_TIMEOUT: Final[float] = 10.0
MAX_RETRIES: Final[int] = 3

# Optimization thresholds
BATCH_SIZE: Final[int] = 512
CACHE_TTL: Final[int] = 3600

# Crypto specific constants
SUPPORTED_NETWORKS: Final[tuple[str, ...]] = (
    'mainnet',
    'testnet',
    'sepolia'
)

# Memory management
GC_COLLECTION_THRESHOLD: Final[int] = 1000

class ChainDefaults:
    GAS_LIMIT: Final[int] = 21000
    MAX_PRIORITY_FEE: Final[int] = 2 * 10**9

def get_batch_limits(item_count: int) -> int:
    return min(item_count, BATCH_SIZE)