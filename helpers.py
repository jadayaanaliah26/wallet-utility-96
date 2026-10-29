import decimal
from typing import Union

def to_wei(amount: Union[int, float, str], decimals: int = 18) -> int:
    context = decimal.Context(prec=80)
    value = decimal.Decimal(str(amount)) * (10 ** decimals)
    return int(value.quantize(decimal.Decimal('1'), rounding=decimal.ROUND_DOWN))

def from_wei(amount: int, decimals: int = 18) -> decimal.Decimal:
    return decimal.Decimal(amount) / (10 ** decimals)

def validate_address(address: str) -> bool:
    if not address.startswith('0x') or len(address) != 42:
        return False
    return all(c in '0123456789abcdefABCDEF' for c in address[2:])

def format_currency(amount: decimal.Decimal, precision: int = 4) -> str:
    return f"{amount:.{precision}f}"