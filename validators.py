import re
from typing import Optional

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    """Validate cryptocurrency address format."""
    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain_type == 'btc':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def validate_amount(amount: str) -> bool:
    """Validate numeric string for crypto transactions."""
    try:
        return float(amount) > 0
    except (ValueError, TypeError):
        return False

def sanitize_memo(memo: Optional[str]) -> str:
    """Remove non-alphanumeric characters from memo."""
    if not memo:
        return ""
    return re.sub(r'[^a-zA-Z0-9 ]', '', memo).strip()