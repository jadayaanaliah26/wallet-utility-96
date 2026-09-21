import re
from decimal import Decimal
from typing import Union


def wei_to_ether(wei_amount: int) -> Decimal:
    if wei_amount < 0:
        raise ValueError("Wei amount cannot be negative")
    return Decimal(wei_amount) / Decimal(10**18)


def ether_to_wei(ether_amount: Union[float, str, Decimal]) -> int:
    amount = Decimal(str(ether_amount))
    if amount < 0:
        raise ValueError("Ether amount cannot be negative")
    return int(amount * Decimal(10**18))


def is_valid_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def truncate_address(address: str, chars: int = 4) -> str:
    if not is_valid_eth_address(address):
        raise ValueError("Invalid Ethereum address format")
    return f"{address[:chars + 2]}...{address[-chars:]}"


def mask_private_key(key: str) -> str:
    clean_key = key.removeprefix("0x")
    if len(clean_key) != 64:
        raise ValueError("Invalid private key length")
    return f"0x{clean_key[:4]}...{clean_key[-4:]}"
