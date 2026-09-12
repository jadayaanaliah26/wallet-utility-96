from typing import Union, Optional
import hashlib


def format_address(address: str) -> str:
    return address.strip().lower()


def validate_checksum(address: str) -> bool:
    if not address.startswith('0x') or len(address) != 42:
        return False
    return address == address.lower()


def calculate_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def wei_to_eth(wei: Union[int, float]) -> float:
    return float(wei) / 10**18


def eth_to_wei(eth: Union[int, float]) -> int:
    return int(float(eth) * 10**18)


def sanitize_input(value: Optional[str]) -> str:
    if not value:
        return ''
    return ''.join(c for c in value if c.isalnum())


def format_transaction_data(to_addr: str, value: int, data: str = '') -> dict:
    return {
        'to': format_address(to_addr),
        'value': value,
        'data': data,
        'gas': 21000
    }