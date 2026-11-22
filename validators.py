import re


def validate_address(address: str) -> bool:
    if not isinstance(address, str) or not (26 <= len(address) <= 35):
        return False
    return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))


def validate_amount(amount: str) -> bool:
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False


def process_transaction(address: str, amount: str):
    if not validate_address(address):
        raise ValueError(f'Invalid wallet address: {address}')
    if not validate_amount(amount):
        raise ValueError(f'Invalid transaction amount: {amount}')
    return {"address": address, "amount": float(amount)}