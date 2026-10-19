from typing import Final

# Network constants
MAINNET_CHAIN_ID: Final = 1
TESTNET_CHAIN_ID: Final = 11155111

# Security constants
MAX_RETRY_ATTEMPTS: Final = 3
DEFAULT_TIMEOUT_SECONDS: Final = 30

# Validation patterns
ADDRESS_PATTERN: Final = r"^0x[a-fA-F0-9]{40}$"
MNEMONIC_WORD_COUNT: Final = 12

# Storage paths
DEFAULT_KEYSTORE_PATH: Final = "./keystore"
ENV_FILE_PATH: Final = ".env"

# Fee estimates
GAS_PRICE_BUFFER: Final = 1.15
PRIORITY_FEE_MULTIPLIER: Final = 1.2

# Error messages
ERR_INVALID_ADDRESS: Final = "invalid wallet address format"
ERR_INSUFFICIENT_FUNDS: Final = "insufficient funds for transaction"
ERR_CONNECTION_TIMEOUT: Final = "blockchain connection timed out"

# Asset identifiers
SUPPORTED_ASSETS: Final = {"ETH", "BTC", "USDT", "USDC"}