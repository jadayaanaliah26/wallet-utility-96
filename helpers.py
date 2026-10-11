import hashlib
import secrets
from typing import Optional

def generate_mnemonic(strength: int = 128) -> str:
    return secrets.token_hex(strength // 8)

def derive_address(public_key: str) -> str:
    sha256 = hashlib.sha256(public_key.encode()).hexdigest()
    return f"0x{hashlib.new('ripemd160', sha256.encode()).hexdigest()}"

def validate_checksum(address: str) -> bool:
    if not address.startswith("0x") or len(address) != 42:
        return False
    return all(c in "0123456789abcdefABCDEF" for c in address[2:])

def format_amount(wei: int, decimals: int = 18) -> float:
    return wei / (10 ** decimals)

def sign_message(private_key: str, message: str) -> str:
    data = message.encode()
    return hashlib.sha256(private_key.encode() + data).hexdigest()