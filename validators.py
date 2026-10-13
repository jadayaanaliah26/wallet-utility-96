import re
from typing import Optional

def validate_address(address: str, chain: str = 'ethereum') -> bool:
    """Validate cryptocurrency wallet address format."""
    if chain == 'ethereum':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain == 'bitcoin':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def validate_amount(amount: str) -> Optional[float]:
    """Validate and convert numeric amount string to float."""
    try:
        val = float(amount)
        return val if val > 0 else None
    except ValueError:
        return None

def is_valid_mnemonic(phrase: str) -> bool:
    """Validate BIP-39 mnemonic phrase length."""
    words = phrase.strip().split()
    return len(words) in [12, 15, 18, 21, 24]

def sanitize_input(data: str) -> str:
    """Remove whitespace and neutralize input characters."""
    return re.sub(r'[^a-zA-Z0-9]', '', data)