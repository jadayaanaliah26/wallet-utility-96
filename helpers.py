import re
from typing import Union


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address or len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def wei_to_eth(wei_value: int) -> float:
    if wei_value < 0:
        raise ValueError("WEI amount cannot be negative")
    return wei_value / 10**18


def eth_to_wei(eth_value: Union[int, float]) -> int:
    if eth_value < 0:
        raise ValueError("ETH amount cannot be negative")
    return int(eth_value * 10**18)


def format_crypto_balance(
    balance: float, decimals: int = 4, symbol: str = ""
) -> str:
    formatted = f"{balance:.{decimals}f}"
    if symbol:
        return f"{formatted} {symbol}".strip()
    return formatted


def is_valid_hex(hex_str: str) -> bool:
    if not isinstance(hex_str, str):
        return False
    clean_hex = hex_str[2:] if hex_str.startswith("0x") else hex_str
    if not clean_hex:
        return False
    return bool(re.fullmatch(r"[0-9a-fA-F]+", clean_hex))
