import re
from decimal import Decimal, InvalidOperation

def validate_address(address):
    if not isinstance(address, str):
        raise TypeError("Address must be string")
    if not address or not address.strip():
        raise ValueError("Address cannot be empty")
    stripped = address.strip()
    if len(stripped) < 26 or len(stripped) > 100:
        raise ValueError("Invalid address length")
    if not re.match(r"^[a-zA-Z0-9]+$", stripped):
        raise ValueError("Address has invalid characters")
    return stripped

def validate_amount(amount):
    if amount is None:
        raise ValueError("Amount cannot be None")
    try:
        dec = Decimal(str(amount))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("Amount must be numeric")
    if dec <= 0:
        raise ValueError("Amount must be greater than zero")
    if dec > Decimal("10000000000"):
        raise ValueError("Amount exceeds maximum allowed")
    return dec

def validate_private_key(key):
    if not isinstance(key, str):
        raise TypeError("Private key must be string")
    if not key:
        raise ValueError("Private key cannot be empty")
    if len(key) != 64:
        raise ValueError("Private key must be 64 characters")
    if not re.match(r"^[0-9a-fA-F]+$", key):
        raise ValueError("Private key must be hexadecimal")
    return key

def validate_wallet(wallet_data):
    if not isinstance(wallet_data, dict):
        raise TypeError("Wallet data must be dict")
    if "address" not in wallet_data:
        raise KeyError("Missing address")
    if "balance" not in wallet_data:
        raise KeyError("Missing balance")
    address = validate_address(wallet_data["address"])
    balance = validate_amount(wallet_data["balance"])
    return {"address": address, "balance": balance}

def validate_transaction(tx):
    if not isinstance(tx, dict):
        raise TypeError("Transaction must be dict")
    for key in ["sender", "recipient", "amount"]:
        if key not in tx:
            raise KeyError(f"Missing {key}")
    validate_address(tx["sender"])
    validate_address(tx["recipient"])
    validate_amount(tx["amount"])
    return tx