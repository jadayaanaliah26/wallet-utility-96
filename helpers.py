from decimal import Decimal
from typing import Union


def parse_units(amount: Union[int, float, str], decimals: int = 18) -> int:
    if isinstance(amount, (int, float)):
        amount = str(amount)
    dec_amount = Decimal(amount)
    multiplier = Decimal(10**decimals)
    return int(dec_amount * multiplier)


def format_units(amount: int, decimals: int = 18) -> str:
    dec_amount = Decimal(amount)
    divisor = Decimal(10**decimals)
    res = dec_amount / divisor
    return f"{res:f}"


def satoshi_to_btc(satoshis: int) -> str:
    return format_units(satoshis, decimals=8)


def btc_to_satoshi(btc: Union[int, float, str]) -> int:
    return parse_units(btc, decimals=8)


def wei_to_eth(wei: int) -> str:
    return format_units(wei, decimals=18)


def eth_to_wei(eth: Union[int, float, str]) -> int:
    return parse_units(eth, decimals=18)


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"
