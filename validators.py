import re
from typing import Union

def is_valid_address(address: str, chain_type: str = 'evm') -> bool:
    if not isinstance(address, str):
        return False
    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain_type == 'btc':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def validate_amount(amount: Union[int, float, str]) -> bool:
    try:
        val = float(amount)
        return val >= 0
    except (ValueError, TypeError):
        return False

def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{64}$', tx_hash))

def sanitize_currency(symbol: str) -> str:
    if not isinstance(symbol, str):
        return ''
    return re.sub(r'[^A-Z0-9]', '', symbol.upper())