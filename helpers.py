import re

ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

def validate_address(address: str) -> bool:
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: str) -> bool:
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(data: dict) -> dict:
    return {
        k: str(v).strip() 
        for k, v in data.items() 
        if v is not None
    }

def process_transaction_data(raw_data: dict):
    data = sanitize_input(raw_data)
    addr = data.get('address')
    amt = data.get('amount')
    
    if not addr or not validate_address(addr):
        raise ValueError(f'invalid address: {addr}')
    
    if not amt or not validate_amount(amt):
        raise ValueError(f'invalid amount: {amt}')
        
    return {'address': addr, 'amount': float(amt)}