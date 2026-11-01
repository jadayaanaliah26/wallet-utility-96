import re
from typing import Optional

def is_valid_address(address: str, chain: str = 'ethereum') -> bool:
    """
    Validate cryptocurrency wallet address formats.
    """
    if chain == 'ethereum':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain == 'bitcoin':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def validate_amount(amount: str) -> Optional[float]:
    """
    Convert and validate transaction amount strings.
    """
    try:
        val = float(amount)
        return val if val > 0 else None
    except ValueError:
        return None

def is_valid_private_key(key: str) -> bool:
    """
    Verify hexadecimal private key structure.
    """
    return bool(re.match(r'^[a-fA-F0-9]{64}$', key))