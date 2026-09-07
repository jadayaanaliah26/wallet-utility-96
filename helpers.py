import hashlib
import secrets
from typing import Optional

def generate_entropy(bits: int = 256) -> bytes:
    return secrets.token_bytes(bits // 8)

def sha256_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def validate_address_format(address: str, prefix: str = '0x') -> bool:
    if not address.startswith(prefix):
        return False
    return len(address[len(prefix):]) == 40 and all(c in '0123456789abcdefABCDEF' for c in address[len(prefix):])

def format_wei_to_eth(wei: int) -> float:
    return wei / 10**18

def format_eth_to_wei(eth: float) -> int:
    return int(eth * 10**18)

def sanitize_hex(value: str) -> str:
    return value.lower().replace('0x', '')

def get_checksum_address(address: str) -> str:
    clean = sanitize_hex(address)
    hashed = sha256_hash(clean.encode()).lower()
    result = ''
    for i in range(len(clean)):
        if int(hashed[i], 16) >= 8:
            result += clean[i].upper()
        else:
            result += clean[i].lower()
    return f'0x{result}'