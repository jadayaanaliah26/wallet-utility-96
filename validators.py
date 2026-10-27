import re

def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.fullmatch(r'0x[a-fA-F0-9]{40}', address))

def validate_amount(amount: float) -> bool:
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_transaction_input(data: dict) -> dict:
    address = data.get('address', '')
    amount = data.get('amount', 0)
    
    if not validate_address(address):
        raise ValueError(f'Invalid wallet address: {address}')
    
    if not validate_amount(amount):
        raise ValueError(f'Invalid transaction amount: {amount}')
    
    return {
        'address': address,
        'amount': float(amount),
        'status': 'validated'
    }