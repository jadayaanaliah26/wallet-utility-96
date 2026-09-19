import re

def validate_address(address: str, chain: str) -> bool:
    patterns = {
        "btc": r"^(bc1|[13])[a-zA-Z0-9]{25,39}$",
        "eth": r"^0x[a-fA-F0-9]{40}$"
    }
    pattern = patterns.get(chain.lower())
    return bool(re.match(pattern, address)) if pattern else False

def validate_amount(amount: str) -> bool:
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_wallet_input(data: dict) -> dict:
    required = ["address", "amount", "chain"]
    if not all(k in data for k in required):
        raise ValueError("missing required fields")
    
    if not validate_address(data["address"], data["chain"]):
        raise ValueError("invalid address format")
    
    if not validate_amount(data["amount"]):
        raise ValueError("invalid transaction amount")
    
    return data