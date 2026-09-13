from typing import Final

# Network identifiers
MAINNET_ID: Final[str] = 'mainnet'
TESTNET_ID: Final[str] = 'testnet'

# Transaction parameters
DEFAULT_GAS_LIMIT: Final[int] = 21000
MIN_CONFIRMATIONS: Final[int] = 6

# Asset constants
ASSET_BTC: Final[str] = 'BTC'
ASSET_ETH: Final[str] = 'ETH'
ASSET_USDT: Final[str] = 'USDT'

# Operational timeouts in seconds
CONNECT_TIMEOUT: Final[float] = 10.0
READ_TIMEOUT: Final[float] = 30.0

# Supported formats
SUPPORTED_ADDRESS_FORMATS: Final[list[str]] = ['bech32', 'p2sh', 'legacy']

def get_chain_config(chain_id: str) -> dict[str, str | int]:
    """Return configuration mapping for a given chain identifier."""
    configs: dict[str, dict[str, str | int]] = {
        MAINNET_ID: {'rpc': 'https://mainnet.infura.io', 'chain_id': 1},
        TESTNET_ID: {'rpc': 'https://sepolia.infura.io', 'chain_id': 11155111}
    }
    return configs.get(chain_id, {})
