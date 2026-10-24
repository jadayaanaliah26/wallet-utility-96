from typing import Final

RPC_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
GAS_LIMIT_BUFFER: Final[float] = 1.2

CURRENCIES: Final[list[str]] = ['BTC', 'ETH', 'SOL']
NETWORKS: Final[dict[str, str]] = {
    'mainnet': 'https://api.mainnet.network',
    'testnet': 'https://api.testnet.network'
}

ERROR_MESSAGES: Final[dict[str, str]] = {
    'insufficient_funds': 'wallet balance below required threshold',
    'connection_error': 'failed to establish network connection',
    'invalid_address': 'provided destination address is malformed'
}

DB_TABLE_NAME: Final[str] = 'wallet_transactions'
DEFAULT_ENCODING: Final[str] = 'utf-8'
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'