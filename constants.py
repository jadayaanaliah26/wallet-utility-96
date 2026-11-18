from enum import Enum
from typing import Dict, Final

DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

SLIPPAGE_TOLERANCE: Final[float] = 0.005
DEFAULT_GAS_LIMIT: Final[int] = 21000
ERC20_GAS_LIMIT: Final[int] = 65000


class ChainID(int, Enum):
    ETHEREUM = 1
    OPTIMISM = 10
    BSC = 56
    POLYGON = 137
    ARBITRUM = 42161
    AVALANCHE = 43114


NATIVE_SYMBOLS: Final[Dict[ChainID, str]] = {
    ChainID.ETHEREUM: "ETH",
    ChainID.OPTIMISM: "ETH",
    ChainID.BSC: "BNB",
    ChainID.POLYGON: "MATIC",
    ChainID.ARBITRUM: "ETH",
    ChainID.AVALANCHE: "AVAX",
}

DEFAULT_RPCS: Final[Dict[ChainID, str]] = {
    ChainID.ETHEREUM: "https://eth.llamarpc.com",
    ChainID.OPTIMISM: "https://mainnet.optimism.io",
    ChainID.BSC: "https://bsc-dataseed.binance.org",
    ChainID.POLYGON: "https://polygon-rpc.com",
    ChainID.ARBITRUM: "https://arb1.arbitrum.io/rpc",
    ChainID.AVALANCHE: "https://api.avax.network/ext/bc/C/rpc",
}

ADDRESS_REGEX: Final[str] = r"^0x[a-fA-F0-9]{40}$"
TX_HASH_REGEX: Final[str] = r"^0x[a-fA-F0-9]{64}$"
