from typing import Union, Optional
from decimal import Decimal

def format_amount(value: Union[int, float, str, Decimal], decimals: int = 8) -> Decimal:
    return Decimal(str(value)).quantize(Decimal(f"1.{'0' * decimals}"))

def validate_address(address: str, prefix: str = "0x") -> bool:
    if not address or not address.startswith(prefix):
        return False
    return len(address) == 42 and address[2:].isalnum()

def calculate_fee(amount: Decimal, rate: float) -> Decimal:
    return (amount * Decimal(str(rate))).quantize(Decimal("1.00000000"))

def mask_address(address: str) -> str:
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"

def to_wei(amount: Union[float, Decimal]) -> int:
    return int(Decimal(str(amount)) * 10**18)

def from_wei(amount: int) -> Decimal:
    return Decimal(amount) / Decimal(10**18)