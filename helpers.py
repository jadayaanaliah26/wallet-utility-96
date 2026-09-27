import re


def wei_to_ether(wei: int) -> float:
    """Convert Wei to Ether.

    Args:
        wei: The amount in Wei to convert.

    Returns:
        The equivalent amount in Ether.
    """
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return wei / 10**18


def ether_to_wei(ether: float) -> int:
    """Convert Ether to Wei.

    Args:
        ether: The amount in Ether to convert.

    Returns:
        The equivalent amount in Wei.
    """
    if ether < 0:
        raise ValueError("Ether amount cannot be negative")
    return int(ether * 10**18)


def is_valid_hex_address(address: str) -> bool:
    """Validate if the string is a standard hexadecimal address format.

    Args:
        address: The string address to validate.

    Returns:
        True if valid hex address, False otherwise.
    """
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def truncate_hash(tx_hash: str, start_chars: int = 6, end_chars: int = 4) -> str:
    """Truncate a transaction hash for display purposes.

    Args:
        tx_hash: The full hash string.
        start_chars: Number of characters to keep at the start.
        end_chars: Number of characters to keep at the end.

    Returns:
        The truncated hash string.
    """
    if not tx_hash.startswith("0x") or len(tx_hash) <= (start_chars + end_chars + 2):
        return tx_hash
    return f"{tx_hash[:start_chars]}...{tx_hash[-end_chars:]}"
