import hashlib
from typing import Optional

def generate_address(public_key: bytes) -> str:
    """Generate a hex-encoded SHA-256 hash address from public key."""
    return hashlib.sha256(public_key).hexdigest()

def validate_checksum(data: bytes, checksum: str) -> bool:
    """Verify data integrity against a provided hex checksum."""
    return hashlib.sha256(data).hexdigest() == checksum

def format_satoshi(amount: int) -> float:
    """Convert satoshi integer to decimal bitcoin unit."""
    return amount / 100_000_000

def mask_address(address: str, visible: int = 4) -> str:
    """Obfuscate address for secure log display."""
    if len(address) <= visible * 2:
        return address
    return f"{address[:visible]}...{address[-visible:]}"

def parse_fee_rate(rate: Optional[str]) -> int:
    """Cast fee rate string to integer base units."""
    return int(rate) if rate and rate.isdigit() else 1000