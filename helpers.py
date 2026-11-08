from decimal import Decimal, ROUND_HALF_UP
from typing import Union


def satoshi_to_btc(satoshis: int) -> Decimal:
    if satoshis < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return (Decimal(satoshis) / Decimal(10**8)).quantize(
        Decimal("0.00000001"), rounding=ROUND_HALF_UP
    )


def btc_to_satoshi(btc: Union[float, str, Decimal]) -> int:
    btc_dec = Decimal(str(btc))
    if btc_dec < 0:
        raise ValueError("BTC amount cannot be negative")
    return int((btc_dec * Decimal(10**8)).to_integral_value(rounding=ROUND_HALF_UP))


def wei_to_eth(wei: int) -> Decimal:
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return (Decimal(wei) / Decimal(10**18)).quantize(
        Decimal("0.00000001"), rounding=ROUND_HALF_UP
    )


def eth_to_wei(eth: Union[float, str, Decimal]) -> int:
    eth_dec = Decimal(str(eth))
    if eth_dec < 0:
        raise ValueError("ETH amount cannot be negative")
    return int((eth_dec * Decimal(10**18)).to_integral_value(rounding=ROUND_HALF_UP))


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address or len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def format_balance(amount: Union[Decimal, float, str], currency: str, decimals: int = 4) -> str:
    val = Decimal(str(amount))
    fmt = f"{{:.{decimals}f}} {{}}"
    return fmt.format(val, currency.upper())
