import hashlib
from decimal import Decimal
from typing import Optional

def validate_address(address: str, prefix: str = '0x') -> bool:
    return address.startswith(prefix) and len(address) == 42

def format_amount(amount: float, decimals: int = 18) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(f'1.{"0" * decimals}'))

def generate_tx_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def get_fee_estimate(gas_limit: int, gas_price: int) -> int:
    return gas_limit * gas_price

def mask_address(address: str) -> str:
    if not address:
        return ''
    return f"{address[:6]}...{address[-4:]}"

def to_wei(amount: float) -> int:
    return int(Decimal(str(amount)) * 10**18)

def from_wei(amount: int) -> Decimal:
    return Decimal(amount) / Decimal(10**18)