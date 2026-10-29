import re

ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

def validate_wallet_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: str) -> bool:
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def process_transaction(data: dict) -> dict:
    address = data.get('address', '')
    amount = data.get('amount', '')

    if not validate_wallet_address(address):
        return {'status': 'error', 'message': 'invalid address format'}

    if not validate_amount(amount):
        return {'status': 'error', 'message': 'invalid transaction amount'}

    return {'status': 'success', 'data': {'address': address, 'amount': float(amount)}}