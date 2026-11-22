import hashlib
import re

ETH_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
TX_HASH_RE = re.compile(r"^(0x)?[a-fA-F0-9]{64}$")
BTC_BASE58_RE = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")


def is_valid_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_RE.match(address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(TX_HASH_RE.match(tx_hash))


def decode_base58(s: str) -> bytes:
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    base = len(alphabet)
    num = 0
    for char in s:
        if char not in alphabet:
            raise ValueError(f"Invalid Base58 character: {char}")
        num = num * base + alphabet.index(char)
    combined = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")
    pad_len = len(s) - len(s.lstrip("1"))
    return b"\x00" * pad_len + combined


def is_valid_btc_legacy_address(address: str) -> bool:
    if not isinstance(address, str) or not BTC_BASE58_RE.match(address):
        return False
    try:
        decoded = decode_base58(address)
        if len(decoded) != 25:
            return False
        payload, checksum = decoded[:-4], decoded[-4:]
        first_hash = hashlib.sha256(payload).digest()
        second_hash = hashlib.sha256(first_hash).digest()
        return second_hash[:4] == checksum
    except ValueError:
        return False


def validate_crypto_data(data_type: str, value: str) -> bool:
    validators = {
        "eth_address": is_valid_eth_address,
        "tx_hash": is_valid_tx_hash,
        "btc_address": is_valid_btc_legacy_address,
    }
    validator = validators.get(data_type)
    if not validator:
        raise ValueError(f"Unsupported data type: {data_type}")
    return validator(value)
