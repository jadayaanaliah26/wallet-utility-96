import hashlib
import hmac
from typing import Optional

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_address(address: str) -> str:
    if not address:
        return ""
    return f"{address[:6]}...{address[-4:]}"

def parse_amount(amount: str) -> float:
    try:
        return float(amount)
    except (ValueError, TypeError):
        return 0.0

def validate_checksum(data: bytes, expected: str) -> bool:
    actual = hashlib.sha256(data).hexdigest()
    return hmac.compare_digest(actual, expected)

def sanitize_currency(symbol: str) -> str:
    return symbol.strip().upper()

def get_fee_basis_points(amount: float, rate: float = 0.001) -> int:
    return int(amount * rate * 10000)