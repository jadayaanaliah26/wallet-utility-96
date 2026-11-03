import hashlib
from decimal import Decimal
from typing import Union

SATOSHI_PER_BITCOIN = 100_000_000
WEI_PER_ETHER = 10**18


def satoshi_to_btc(satoshi: int) -> Decimal:
    return Decimal(satoshi) / Decimal(SATOSHI_PER_BITCOIN)


def btc_to_satoshi(btc: Union[float, str, Decimal]) -> int:
    return int(Decimal(str(btc)) * SATOSHI_PER_BITCOIN)


def wei_to_ether(wei: int) -> Decimal:
    return Decimal(wei) / Decimal(WEI_PER_ETHER)


def ether_to_wei(ether: Union[float, str, Decimal]) -> int:
    return int(Decimal(str(ether)) * WEI_PER_ETHER)


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()
