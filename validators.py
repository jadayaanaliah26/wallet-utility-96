import re
from typing import Any

class WalletValidationError(Exception):
    pass

def validate_address(address: str) -> None:
    if not isinstance(address, str):
        raise WalletValidationError("Address must be a string")
    if not re.fullmatch(r'0x[a-fA-F0-9]{40}', address):
        raise WalletValidationError("Invalid ethereum address format")

def validate_amount(amount: Any) -> None:
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise WalletValidationError("Amount must be a positive number")

def validate_transaction_payload(payload: dict) -> None:
    required_fields = {"address", "amount", "token"}
    if not isinstance(payload, dict):
        raise WalletValidationError("Payload must be a dictionary")
    if not required_fields.issubset(payload.keys()):
        missing = required_fields - payload.keys()
        raise WalletValidationError(f"Missing fields: {missing}")
    
    validate_address(payload["address"])
    validate_amount(payload["amount"])
