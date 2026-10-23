import re

ADDRESS_PATTERNS = {
    'btc': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$',
    'eth': r'^0x[a-fA-F0-9]{40}$'
}

def validate_address(address: str, chain: str) -> bool:
    pattern = ADDRESS_PATTERNS.get(chain.lower())
    if not pattern:
        raise ValueError(f"unsupported chain: {chain}")
    return bool(re.match(pattern, address))

def sanitize_amount(amount: str) -> float:
    try:
        value = float(amount)
        if value < 0:
            return 0.0
        return value
    except (ValueError, TypeError):
        return 0.0

def validate_transaction_hex(tx_hex: str) -> bool:
    if not isinstance(tx_hex, str):
        return False
    return bool(re.fullmatch(r'^[0-9a-fA-F]+$', tx_hex))