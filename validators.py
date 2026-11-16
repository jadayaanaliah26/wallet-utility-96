from typing import Optional

class ValidationError(Exception):
    pass

def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        raise ValidationError('address must be a string')
    if len(address) < 26 or len(address) > 35:
        raise ValidationError('invalid address length')
    if not address.isalnum():
        raise ValidationError('address contains invalid characters')
    return True

def validate_amount(amount: float) -> bool:
    if not isinstance(amount, (int, float)):
        raise ValidationError('amount must be numeric')
    if amount <= 0:
        raise ValidationError('amount must be positive')
    return True

def sanitize_input(value: Optional[str]) -> str:
    if value is None:
        return ''
    return str(value).strip()