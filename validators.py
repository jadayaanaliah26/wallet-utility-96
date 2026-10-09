import re
from typing import Optional

class ValidationError(Exception):
    pass

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    if not address or not isinstance(address, str):
        raise ValidationError('Address must be a non-empty string')

    if chain_type == 'evm':
        if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
            raise ValidationError('Invalid EVM address format')
    elif chain_type == 'btc':
        if not re.match(r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$', address):
            raise ValidationError('Invalid BTC address format')
    else:
        raise ValueError(f'Unsupported chain type: {chain_type}')

    return True

def validate_amount(amount: str) -> float:
    try:
        val = float(amount)
        if val <= 0:
            raise ValidationError('Amount must be positive')
        return val
    except (ValueError, TypeError):
        raise ValidationError('Invalid numeric amount')

def validate_gas_price(gwei: float) -> bool:
    if gwei < 0.0001 or gwei > 5000:
        raise ValidationError('Gas price out of sensible bounds')
    return True