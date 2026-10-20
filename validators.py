import re
from typing import Any, Dict


class ValidationError(Exception):
    pass


def validate_address(address: str, chain: str = "eth") -> bool:
    if not isinstance(address, str) or not address:
        raise ValidationError("Address must be a non-empty string")

    patterns = {
        "eth": r"^0x[a-fA-F0-9]{40}$",
        "btc": r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$",
    }

    pattern = patterns.get(chain.lower())
    if not pattern:
        raise ValidationError(f"Unsupported chain: {chain}")

    if not re.match(pattern, address):
        raise ValidationError(f"Invalid {chain.upper()} address format")
    return True


def validate_amount(amount: Any, max_limit: float = 1e6) -> float:
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise ValidationError("Amount must be a numeric value")

    if val <= 0:
        raise ValidationError("Amount must be greater than zero")
    if val > max_limit:
        raise ValidationError(f"Amount exceeds maximum limit of {max_limit}")
    return val


def validate_transaction_input(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("Input payload must be a dictionary")

    required_keys = {"recipient", "amount", "chain"}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

    validate_address(data["recipient"], data["chain"])
    validated_amount = validate_amount(data["amount"])

    return {
        "recipient": data["recipient"],
        "amount": validated_amount,
        "chain": data["chain"].lower(),
    }