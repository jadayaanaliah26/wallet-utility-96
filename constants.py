from typing import Final

# Network identifiers
MAINNET_ID: Final[str] = "mainnet"
TESTNET_ID: Final[str] = "testnet"

# Security configurations
MIN_PASSWORD_LENGTH: Final[int] = 12
PBKDF2_ITERATIONS: Final[int] = 600000
AES_KEY_SIZE: Final[int] = 32

# API endpoints and defaults
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

# Formatting defaults
DECIMAL_PRECISION: Final[int] = 8
CURRENCY_SYMBOL: Final[str] = "$"

# Error messages
ERR_INVALID_ADDRESS: Final[str] = "invalid wallet address format"
ERR_INSUFFICIENT_FUNDS: Final[str] = "insufficient funds for transaction"
ERR_CONNECTION_FAILED: Final[str] = "network connection request failed"

# Supported protocols
SUPPORTED_NETWORKS: Final[list[str]] = [MAINNET_ID, TESTNET_ID]