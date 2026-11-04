import hashlib
from typing import Optional

def generate_address(public_key: bytes) -> str:
    """Generate a hex-encoded SHA-256 address from public key."""
    return hashlib.sha256(public_key).hexdigest()

def validate_checksum(data: str, checksum: str) -> bool:
    """Verify data integrity against a provided SHA-256 checksum."""
    return hashlib.sha256(data.encode()).hexdigest() == checksum

def format_amount(amount: float, precision: int = 8) -> str:
    """Convert float amount to string with fixed decimal precision."""
    return f"{amount:.{precision}f}"

def parse_derivation_path(path: str) -> list[int]:
    """Convert BIP32 derivation path string to integer sequence."""
    return [int(x.replace("'", "")) for x in path.split("/")[1:]]

def sanitize_memo(memo: Optional[str]) -> str:
    """Normalize transaction memo string for protocol requirements."""
    if not memo:
        return ""
    return memo.strip()[:64]