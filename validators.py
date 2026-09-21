import re

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) not in (26, 42):
        return False
    return bool(re.match(r'^[a-zA-Z0-9]+$', address))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def process_wallet_input(data: dict) -> dict:
    address = data.get("address")
    amount = data.get("amount")
    
    if not validate_address(address):
        raise ValueError("invalid wallet address format")
    if not validate_amount(amount):
        raise ValueError("invalid transaction amount")
    
    return {"status": "valid", "address": address, "amount": float(amount)}

def run_processing_loop(inputs: list) -> list:
    results = []
    for entry in inputs:
        try:
            results.append(process_wallet_input(entry))
        except (ValueError, TypeError):
            continue
    return results