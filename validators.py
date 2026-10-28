import re
from typing import Union


class WalletValidationError(ValueError):
    pass


class InvalidAddressError(WalletValidationError):
    pass


class InvalidAmountError(WalletValidationError):
    pass


def validate_ethereum_address(address: str) -> str:
    if not isinstance(address, str):
        raise InvalidAddressError("Address must be a string")
    cleaned = address.strip()
    if not cleaned:
        raise InvalidAddressError("Address cannot be empty")
    if not re.match(r"^0x[a-fA-F0-9]{40}$", cleaned):
        raise InvalidAddressError("Invalid Ethereum address format")
    return cleaned


def validate_transaction_amount(
    amount: Union[int, float, str], min_amount: float = 0.0001
) -> float:
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise InvalidAmountError("Amount must be numeric")

    if val != val or val in (float("inf"), float("-inf")):
        raise InvalidAmountError("Amount must be a finite non-NaN number")

    if val <= 0:
        raise InvalidAmountError("Amount must be positive")

    if val < min_amount:
        raise InvalidAmountError(f"Amount below minimum threshold: {min_amount}")

    return val


def validate_hex_seed(seed: str) -> str:
    if not isinstance(seed, str):
        raise WalletValidationError("Seed must be a string")
    cleaned = seed.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    if len(cleaned) not in (64, 128):
        raise WalletValidationError("Hex seed must be 64 or 128 characters")
    if not re.match(r"^[a-f0-9]+$", cleaned):
        raise WalletValidationError("Seed contains non-hexadecimal characters")
    return cleaned
