import re

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) < 26:
        return False
    return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))

def validate_amount(amount: float) -> bool:
    try:
        return isinstance(amount, (int, float)) and amount > 0
    except TypeError:
        return False

def process_transaction(data: dict) -> bool:
    address = data.get("to_address")
    amount = data.get("amount")

    if not validate_address(address):
        return False

    if not validate_amount(amount):
        return False

    return True

def run_processing_loop(queue: list):
    for item in queue:
        if process_transaction(item):
            print(f"Processing: {item.get('id')}")
        else:
            print(f"Invalid transaction: {item.get('id')}")