import re
from typing import Union

ETH_DECIMALS = 18
BTC_DECIMALS = 8


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address or len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def wei_to_ether(wei: int) -> float:
    if wei < 0:
        raise ValueError("Amount cannot be negative")
    return wei / (10**ETH_DECIMALS)


def ether_to_wei(ether: Union[int, float]) -> int:
    if ether < 0:
        raise ValueError("Amount cannot be negative")
    return int(ether * (10**ETH_DECIMALS))


def sat_to_btc(satoshis: int) -> float:
    if satoshis < 0:
        raise ValueError("Amount cannot be negative")
    return satoshis / (10**BTC_DECIMALS)


def btc_to_sat(btc: Union[int, float]) -> int:
    if btc < 0:
        raise ValueError("Amount cannot be negative")
    return int(btc * (10**BTC_DECIMALS))


def is_valid_hex(value: str) -> bool:
    if not isinstance(value, str):
        return False
    clean_val = value[2:] if value.startswith("0x") else value
    return bool(re.fullmatch(r"[0-9a-fA-F]*", clean_val)) and len(clean_val) % 2 == 0
