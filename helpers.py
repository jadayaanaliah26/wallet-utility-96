import hashlib
import secrets
from typing import Union


def wei_to_ether(wei: int) -> float:
    return wei / 10**18


def ether_to_wei(ether: Union[float, int]) -> int:
    return int(ether * 10**18)


def satoshi_to_btc(satoshi: int) -> float:
    return satoshi / 10**8


def btc_to_satoshi(btc: Union[float, int]) -> int:
    return int(btc * 10**8)


def generate_private_key() -> str:
    return secrets.token_hex(32)


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def is_valid_hex_address(address: str, length: int = 40) -> bool:
    clean_addr = address.lower()
    if clean_addr.startswith("0x"):
        clean_addr = clean_addr[2:]
    if len(clean_addr) != length:
        return False
    try:
        int(clean_addr, 16)
        return True
    except ValueError:
        return False
