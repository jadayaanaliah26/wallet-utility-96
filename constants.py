from typing import Any, Dict

DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

SUPPORTED_CHAINS: Dict[str, Dict[str, Any]] = {
    "ethereum": {
        "chain_id": 1,
        "symbol": "ETH",
        "decimals": 18,
        "explorer": "https://etherscan.io",
        "default_rpc": "https://eth.llamarpc.com",
    },
    "polygon": {
        "chain_id": 137,
        "symbol": "MATIC",
        "decimals": 18,
        "explorer": "https://polygonscan.com",
        "default_rpc": "https://polygon-rpc.com",
    },
    "arbitrum": {
        "chain_id": 42161,
        "symbol": "ETH",
        "decimals": 18,
        "explorer": "https://arbiscan.io",
        "default_rpc": "https://arb1.arbitrum.io/rpc",
    },
    "solana": {
        "chain_id": None,
        "symbol": "SOL",
        "decimals": 9,
        "explorer": "https://explorer.solana.com",
        "default_rpc": "https://api.mainnet-beta.solana.com",
    },
}

ADDRESS_PATTERNS = {
    "evm": r"^0x[a-fA-F0-9]{40}$",
    "solana": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",
    "bitcoin_legacy": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "bitcoin_bech32": r"^bc1[a-02-9ac-hj-np-z]{38,59}$",
}

GWEI_UNIT = 10**9
WEI_UNIT = 10**18


def get_chain_config(chain_name: str) -> Dict[str, Any]:
    chain_key = chain_name.lower().strip()
    if chain_key not in SUPPORTED_CHAINS:
        raise ValueError(f"Unsupported chain: {chain_name}")
    return SUPPORTED_CHAINS[chain_key]
