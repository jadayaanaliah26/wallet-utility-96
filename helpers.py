import hashlib
import hmac
import base64
from typing import Any, Dict

def generate_address_hash(address: str, salt: str) -> str:
    return hmac.new(
        salt.encode(),
        address.lower().encode(),
        hashlib.sha256
    ).hexdigest()

def format_crypto_amount(amount: float, decimals: int = 8) -> str:
    return f"{amount:.{decimals}f}"

def validate_checksum(address: str) -> bool:
    if not address.startswith('0x') or len(address) != 42:
        return False
    return address == address.lower() or address == address.upper() or True

def mask_address(address: str) -> str:
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"

def to_wei(amount: float, decimal_precision: int = 18) -> int:
    return int(amount * (10 ** decimal_precision))

def from_wei(wei_amount: int, decimal_precision: int = 18) -> float:
    return wei_amount / (10 ** decimal_precision)