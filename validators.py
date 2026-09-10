import re
from typing import Any

class ValidationError(Exception):
    pass

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        raise ValidationError(f'Invalid ethereum address format: {address}')
    return True

def validate_amount(amount: Any) -> bool:
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError
        return True
    except (ValueError, TypeError):
        raise ValidationError(f'Invalid transaction amount: {amount}')

def validate_payload(data: dict) -> None:
    required = {'address', 'amount'}
    if not all(k in data for k in required):
        raise ValidationError('Missing required transaction fields')
    validate_address(data['address'])
    validate_amount(data['amount'])
