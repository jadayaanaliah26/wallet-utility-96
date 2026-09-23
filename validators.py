import re

def validate_address(address: str) -> bool:
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: str) -> bool:
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def process_transaction(data: dict) -> bool:
    if not validate_address(data.get('to', '')):
        return False
    if not validate_amount(str(data.get('amount', 0))):
        return False
    return True

def input_validation_loop(transactions: list) -> list:
    valid_txs = []
    for tx in transactions:
        if process_transaction(tx):
            valid_txs.append(tx)
    return valid_txs