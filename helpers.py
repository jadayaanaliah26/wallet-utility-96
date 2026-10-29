from decimal import Decimal, ROUND_HALF_UP
from typing import Union


def format_crypto_amount(amount: Union[str, float, Decimal], precision: int = 8) -> Decimal:
    """Normalize crypto amounts to fixed decimal precision."""
    return Decimal(str(amount)).quantize(Decimal(f"1.{'0' * precision}"), rounding=ROUND_HALF_UP)


def calculate_fee(amount: Union[str, float, Decimal], rate: float) -> Decimal:
    """Calculate transaction fee based on percentage rate."""
    val = Decimal(str(amount))
    fee = val * Decimal(str(rate))
    return fee.quantize(Decimal("1.00000000"), rounding=ROUND_HALF_UP)


def validate_address(address: str, chain: str) -> bool:
    """Address validation logic for supported networks."""
    validators = {
        "btc": lambda a: a.startswith(('1', '3', 'bc1')),
        "eth": lambda a: a.startswith('0x') and len(a) == 42
    }
    validator = validators.get(chain.lower())
    return validator(address) if validator else False


def get_dust_threshold(symbol: str) -> Decimal:
    """Minimum amount threshold for small balance dusting."""
    thresholds = {"BTC": "0.00001", "ETH": "0.001", "SOL": "0.01"}
    return Decimal(thresholds.get(symbol.upper(), "0.0001"))