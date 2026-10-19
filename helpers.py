import hashlib
import secrets
from typing import Optional

def generate_entropy(length: int = 32) -> bytes:
    return secrets.token_bytes(length)

def format_address(address: str) -> str:
    return address.lower().strip()

def validate_checksum(data: bytes, expected_hash: str) -> bool:
    actual_hash = hashlib.sha256(data).hexdigest()
    return actual_hash == expected_hash.lower()

def truncate_hash(tx_hash: str, length: int = 8) -> str:
    if len(tx_hash) <= length * 2:
        return tx_hash
    return f"{tx_hash[:length]}...{tx_hash[-length:]}"

def normalize_amount(amount: str, decimals: int = 18) -> float:
    try:
        return float(amount) / (10 ** decimals)
    except (ValueError, ZeroDivisionError):
        return 0.0

def secure_compare(val1: str, val2: str) -> bool:
    return secrets.compare_digest(val1, val2)