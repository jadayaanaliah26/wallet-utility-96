from typing import Union
from decimal import Decimal, ROUND_HALF_UP


def format_amount(amount: Union[str, float, Decimal], decimals: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(f'1.{"0" * decimals}'), rounding=ROUND_HALF_UP)


def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return address.startswith('0x') and len(address) == 42


def satoshis_to_btc(sats: int) -> Decimal:
    return Decimal(sats) / Decimal('100000000')


def btc_to_satoshis(btc: Union[str, float, Decimal]) -> int:
    return int(Decimal(str(btc)) * Decimal('100000000'))


def mask_address(address: str) -> str:
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"


def calculate_fee(amount: Decimal, rate: Decimal) -> Decimal:
    return (amount * rate).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)