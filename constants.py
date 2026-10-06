from enum import Enum
from typing import Dict, Set

class ChainID(Enum):
    ETHEREUM = 1
    POLYGON = 137
    BSC = 56

COIN_TICKERS: Set[str] = {'ETH', 'MATIC', 'BNB', 'USDT', 'USDC'}

PRECISION_MAP: Dict[str, int] = {
    'ETH': 18,
    'MATIC': 18,
    'BNB': 18,
    'USDT': 6,
    'USDC': 6
}

DEFAULT_TIMEOUT: float = 30.0
MAX_RETRIES: int = 3

RPC_ENDPOINTS: Dict[ChainID, str] = {
    ChainID.ETHEREUM: "https://ethereum.publicnode.com",
    ChainID.POLYGON: "https://polygon.llamarpc.com",
    ChainID.BSC: "https://bsc-dataseed.binance.org"
}

DECIMALS_DEFAULT: int = 18
MIN_GAS_LIMIT: int = 21000