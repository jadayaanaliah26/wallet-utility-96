import hashlib
import secrets
from typing import Optional

def generate_wallet_address(public_key: bytes) -> str:
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160', sha256_hash).digest()
    return ripemd160.hex()

def validate_checksum(address: str) -> bool:
    if len(address) != 40:
        return False
    try:
        int(address, 16)
        return True
    except ValueError:
        return False

def create_secure_nonce(length: int = 32) -> str:
    return secrets.token_hex(length)

def format_satoshi_to_btc(satoshi: int) -> float:
    return float(satoshi / 100_000_000)

def format_btc_to_satoshi(btc: float) -> int:
    return int(btc * 100_000_000)

def sign_transaction_payload(payload: str, private_key: str) -> str:
    message = payload.encode()
    signature = hashlib.sha256(message + private_key.encode()).hexdigest()
    return signature