import hashlib
import hmac
from typing import Optional

def generate_address_checksum(address: str) -> str:
    """Checksum verification for hex addresses."""
    address = address.lower().replace("0x", "")
    address_hash = hashlib.sha3_256(address.encode()).hexdigest()
    checksum = "0x"
    for i in range(len(address)):
        if int(address_hash[i], 16) >= 8:
            checksum += address[i].upper()
        else:
            checksum += address[i]
    return checksum

def validate_mnemonic(mnemonic: str) -> bool:
    """Validation logic for bip39 phrases."""
    parts = mnemonic.split()
    return len(parts) in [12, 24]

def derive_key_path(path: str) -> Optional[list[int]]:
    """Transformation of derivation strings to indices."""
    try:
        return [int(x.rstrip("'")) for x in path.split("/")[1:]]
    except (ValueError, AttributeError):
        return None

def sanitize_input(value: str) -> str:
    """Standardization of hexadecimal input strings."""
    return value.strip().lower()