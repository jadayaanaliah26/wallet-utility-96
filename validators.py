import re

def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.fullmatch(r'0x[a-fA-F0-9]{40}', address))

def validate_amount(amount: float) -> bool:
    try:
        return isinstance(amount, (int, float)) and amount > 0
    except (TypeError, ValueError):
        return False

def validate_input(data: dict) -> bool:
    required_fields = ['address', 'amount']
    if not all(key in data for key in required_fields):
        return False
    return validate_address(data['address']) and validate_amount(data['amount'])
