import re
from typing import Dict, Union


class WalletError(Exception):
    pass


class InvalidAddressError(WalletError):
    pass


class InvalidAmountError(WalletError):
    pass


def parse_transaction_input(address: str, amount: Union[int, float, str]) -> Dict[str, Union[str, float]]:
    if not isinstance(address, str):
        raise InvalidAddressError("Wallet address must be a string")

    address = address.strip()
    if not address:
        raise InvalidAddressError("Wallet address cannot be empty")

    if address.startswith("0x"):
        if not re.fullmatch(r"0x[a-fA-F0-9]{40}", address):
            raise InvalidAddressError("Malformed Ethereum address format")
    elif address.startswith(("1", "3", "bc1")):
        if not (26 <= len(address) <= 62) or not re.fullmatch(r"[a-zA-Z0-9]+", address):
            raise InvalidAddressError("Malformed Bitcoin address format")
    else:
        raise InvalidAddressError("Unsupported cryptocurrency address format")

    try:
        numeric_amount = float(amount)
    except (ValueError, TypeError):
        raise InvalidAmountError(f"Invalid numeric amount value: {amount}")

    if numeric_amount <= 0:
        raise InvalidAmountError("Transaction amount must be strictly positive")

    if numeric_amount > 1e9:
        raise InvalidAmountError("Transaction amount exceeds maximum limit")

    return {
        "address": address,
        "amount": round(numeric_amount, 8),
        "network": "ethereum" if address.startswith("0x") else "bitcoin",
    }
