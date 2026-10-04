import hashlib
from decimal import Decimal
from typing import Union

def format_amount(amount: Union[int, float, str], decimals: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(10) ** -decimals)

def generate_address_hash(pubkey: str) -> str:
    sha256 = hashlib.sha256(pubkey.encode()).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).hexdigest()
    return ripemd160

def validate_fee_rate(rate: float) -> bool:
    return 0.00000001 <= rate <= 0.1

def mask_key(key: str) -> str:
    if len(key) < 8:
        return "****"
    return f"{key[:4]}{'*' * (len(key) - 8)}{key[-4:]}"

def to_satoshi(amount: Union[float, Decimal]) -> int:
    return int(Decimal(str(amount)) * 10**8)

def from_satoshi(satoshi: int) -> Decimal:
    return Decimal(satoshi) / Decimal(10**8)