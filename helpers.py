from typing import Union


def format_checksum_address(address: str) -> str:
    """Format a crypto wallet address by stripping whitespace and converting to lowercase.

    Args:
        address: Raw blockchain wallet address string.

    Returns:
        Cleaned address string.
    """
    if not isinstance(address, str):
        raise TypeError("Address must be a string")
    return address.strip().lower()


def satoshi_to_btc(satoshis: int) -> float:
    """Convert standard Satoshi units to Bitcoin.

    Args:
        satoshis: Amount in Satoshis (1 BTC = 100,000,000 Satoshis).

    Returns:
        Equivalent value in BTC.
    """
    if satoshis < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return satoshis / 100_000_000.0


def btc_to_satoshi(btc: Union[int, float]) -> int:
    """Convert Bitcoin amount to Satoshis.

    Args:
        btc: Amount in BTC.

    Returns:
        Equivalent value in Satoshis.
    """
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(round(btc * 100_000_000))


def mask_address(address: str, visible_chars: int = 4) -> str:
    """Mask a public wallet address for display showing prefix and suffix.

    Args:
        address: Full public address string.
        visible_chars: Number of characters to display at start and end.

    Returns:
        Masked address string with ellipsis.
    """
    clean_addr = address.strip()
    if len(clean_addr) <= visible_chars * 2:
        return clean_addr
    return f"{clean_addr[:visible_chars]}...{clean_addr[-visible_chars:]}"
