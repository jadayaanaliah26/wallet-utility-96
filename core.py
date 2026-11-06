import hashlib
import base58
from typing import Optional

def validate_address(address: str, prefix: str = '1') -> bool:
    try:
        decoded = base58.b58decode_check(address)
        return decoded.startswith(prefix.encode())
    except Exception:
        return False

def generate_checksum(data: bytes) -> str:
    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()

def format_wei(value: int, decimals: int = 18) -> float:
    return float(value) / (10 ** decimals)

def mask_address(address: str) -> str:
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"

def derive_derivation_path(index: int) -> str:
    return f"m/44'/60'/0'/0/{index}"