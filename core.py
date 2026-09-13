from typing import Union
import hashlib
import hmac

def generate_address_hash(address: str, secret: str) -> str:
    return hmac.new(
        secret.encode(),
        address.encode(),
        hashlib.sha256
    ).hexdigest()

def format_amount(amount: Union[int, float], decimals: int = 8) -> str:
    return f"{amount:.{decimals}f}".rstrip('0').rstrip('.')

def validate_checksum(address: str) -> bool:
    if not address.startswith('0x') or len(address) != 42:
        return False
    return address[2:].isalnum()

def calculate_fee(amount: float, rate: float, min_fee: float) -> float:
    return max(amount * rate, min_fee)

def mask_address(address: str) -> str:
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"