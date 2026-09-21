from decimal import Decimal
from typing import Union


def satoshi_to_btc(satoshi: int) -> Decimal:
    """Convert an amount in Satoshi to Bitcoin.

    Args:
        satoshi: Integer amount in Satoshi.

    Returns:
        Decimal representation in Bitcoin.
    """
    if satoshi < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return Decimal(satoshi) / Decimal(100_000_000)


def btc_to_satoshi(btc: Union[int, float, str, Decimal]) -> int:
    """Convert an amount in Bitcoin to Satoshi.

    Args:
        btc: Bitcoin amount as int, float, str, or Decimal.

    Returns:
        Integer amount in Satoshi.
    """
    amount = Decimal(str(btc))
    if amount < 0:
        raise ValueError("Bitcoin amount cannot be negative")
    return int(amount * Decimal(100_000_000))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate a cryptocurrency address for display purposes.

    Args:
        address: Full blockchain address string.
        prefix_len: Number of characters to keep at start.
        suffix_len: Number of characters to keep at end.

    Returns:
        Truncated address formatted with ellipsis.
    """
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def is_valid_hex_key(key: str, expected_bytes: int = 32) -> bool:
    """Validate if a string is a valid hexadecimal key of expected byte length.

    Args:
        key: Hexadecimal string to check.
        expected_bytes: Expected length in bytes.

    Returns:
        True if key is valid hex and matches expected byte length.
    """
    clean_key = key.removeprefix("0x")
    if len(clean_key) != expected_bytes * 2:
        return False
    try:
        int(clean_key, 16)
        return True
    except ValueError:
        return False