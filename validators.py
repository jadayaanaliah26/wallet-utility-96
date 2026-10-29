import re
from typing import Union

def validate_address(address: str, chain: str = 'ethereum') -> bool:
    patterns = {
        'ethereum': r'^0x[a-fA-F0-9]{40}$',
        'bitcoin': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$'
    }
    pattern = patterns.get(chain.lower())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def validate_amount(amount: Union[int, float, str]) -> bool:
    try:
        val = float(amount)
        return val >= 0
    except (ValueError, TypeError):
        return False

def sanitize_currency_code(code: str) -> str:
    if not isinstance(code, str):
        return ''
    clean = re.sub(r'[^A-Z]', '', code.upper())
    return clean if 2 <= len(clean) <= 5 else ''

def check_tx_hex(tx_hash: str) -> bool:
    return bool(re.match(r'^[a-fA-F0-9]{64}$', tx_hash))