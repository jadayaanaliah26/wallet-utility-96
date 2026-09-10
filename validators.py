import re

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

class ValidationError(Exception):
    pass

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or not ADDRESS_PATTERN.match(address):
        raise ValidationError(f'Invalid ethereum address format: {address}')
    return True

def validate_amount(amount: float) -> bool:
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValidationError(f'Invalid transaction amount: {amount}')
    return True

def validate_payload(data: dict) -> None:
    required = ['recipient', 'amount']
    for field in required:
        if field not in data:
            raise ValidationError(f'Missing required field: {field}')
    
    validate_address(data['recipient'])
    validate_amount(data['amount'])
