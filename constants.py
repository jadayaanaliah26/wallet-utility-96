"""Constants and configuration defaults for crypto wallet utilities."""

from enum import Enum
from typing import Dict, Final


class Network(str, Enum):
    """Supported blockchain networks."""

    ETHEREUM = "ethereum"
    POLYGON = "polygon"
    ARBITRUM = "arbitrum"
    OPTIMISM = "optimism"
    SOLANA = "solana"


CHAIN_IDS: Final[Dict[Network, int]] = {
    Network.ETHEREUM: 1,
    Network.POLYGON: 137,
    Network.ARBITRUM: 42161,
    Network.OPTIMISM: 10,
}

DEFAULT_GAS_LIMITS: Final[Dict[str, int]] = {
    "transfer": 21000,
    "erc20_transfer": 65000,
    "uniswap_swap": 200000,
}

WEI_PER_ETH: Final[int] = 10**18
GWEI_PER_ETH: Final[int] = 10**9
SATOSHIS_PER_BTC: Final[int] = 10**8

ADDRESS_PATTERNS: Final[Dict[str, str]] = {
    "evm": r"^0x[a-fA-F0-9]{40}$",
    "btc_legacy": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "btc_bech32": r"^bc1[a-02-9ac-hj-np-z]{38,59}$",
    "solana": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",
}


def get_chain_id(network: Network) -> int:
    """Return the EIP-155 chain ID for a given network.

    Args:
        network: The network identifier.

    Returns:
        The integer chain ID.

    Raises:
        KeyError: If the network is non-EVM or unsupported.
    """
    return CHAIN_IDS[network]
