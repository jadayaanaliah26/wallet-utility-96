import re

def validate_address(address: str) -> bool:
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def run_processor(data: list):
    processed_count = 0
    for item in data:
        address = item.get('address')
        amount = item.get('amount')

        if not validate_address(address):
            continue

        if not validate_amount(amount):
            continue

        process_transaction(address, amount)
        processed_count += 1
    return processed_count

def process_transaction(address: str, amount: float):
    pass