import re

EVM_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_REGEX = re.compile(
    r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-0-9ac-hj-np-z]{8,87})$"
)
HEX_KEY_REGEX = re.compile(r"^(0x)?[a-fA-F0-9]{64}$")


def is_valid_evm_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(EVM_ADDRESS_REGEX.match(address))


def is_valid_btc_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_REGEX.match(address))


def is_valid_private_key(key: str) -> bool:
    if not isinstance(key, str):
        return False
    return bool(HEX_KEY_REGEX.match(key))


def is_valid_transaction_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    clean_hash = tx_hash[2:] if tx_hash.startswith("0x") else tx_hash
    return len(clean_hash) == 64 and all(c in "0123456789abcdefABCDEF" for c in clean_hash)


def sanitize_hex_string(hex_str: str) -> str:
    if not isinstance(hex_str, str):
        raise ValueError("Input must be a string")
    cleaned = hex_str.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    if len(cleaned) % 2 != 0:
        cleaned = "0" + cleaned
    if not all(c in "0123456789abcdef" for c in cleaned):
        raise ValueError("Invalid hex character encountered")
    return f"0x{cleaned}"
