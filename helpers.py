import hashlib
from typing import Optional

def generate_address(public_key: bytes) -> str:
    """Generate a hex-encoded crypto wallet address from public key."""
    sha256_hash: bytes = hashlib.sha256(public_key).digest()
    ripemd160: hashlib._Hash = hashlib.new("ripemd160")
    ripemd160.update(sha256_hash)
    return ripemd160.hexdigest()

def validate_checksum(address: str, checksum: str) -> bool:
    """Verify integrity of wallet address against provided checksum."""
    computed: str = hashlib.sha256(address.encode()).hexdigest()[:8]
    return computed == checksum

def format_balance(amount: float, precision: int = 8) -> str:
    """Convert float balance to zero-padded string representation."""
    template: str = f":.{precision}f"
    return format(amount, template)

def mask_private_key(key: str) -> str:
    """Obfuscate private key for secure logging purposes."""
    if len(key) < 8:
        return "***"
    return f"{key[:4]}...{key[-4:]}"

def parse_fee_rate(fee_input: Optional[str]) -> float:
    """Convert fee input string to float or default base rate."""
    if not fee_input:
        return 0.0001
    try:
        return float(fee_input)
    except ValueError:
        return 0.0001