from decimal import Decimal

CURRENCIES = {
    "BTC": {
        "decimals": 8,
        "min_tx": Decimal("0.0001"),
        "fee_rate": Decimal("0.00001")
    },
    "ETH": {
        "decimals": 18,
        "min_tx": Decimal("0.001"),
        "fee_rate": Decimal("0.00005")
    },
    "SOL": {
        "decimals": 9,
        "min_tx": Decimal("0.01"),
        "fee_rate": Decimal("0.000005")
    }
}

RPC_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_NETWORK = "mainnet"

ERROR_CODES = {
    "INSUFFICIENT_FUNDS": 1001,
    "INVALID_ADDRESS": 1002,
    "NETWORK_UNREACHABLE": 1003,
    "RATE_LIMIT_EXCEEDED": 1004
}

BLOCKCHAIN_EXPLORERS = {
    "BTC": "https://blockstream.info",
    "ETH": "https://etherscan.io",
    "SOL": "https://explorer.solana.com"
}