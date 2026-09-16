import re

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_address(address: str) -> bool:
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def validate_payload(data: dict) -> bool:
    required = ['address', 'amount']
    if not all(key in data for key in required):
        return False
    return validate_address(data['address']) and validate_amount(data['amount'])