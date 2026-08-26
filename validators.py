import re


def is_valid_bitcoin_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    
    legacy_regex = r"^(1|3)[a-km-zA-HJ-NP-Z1-9]{25,34}$"
    bech32_regex = r"^(bc1)[0-aa-hj-np-z0-9]{39,59}$"
    
    return bool(re.match(legacy_regex, address) or re.match(bech32_regex, address))


def is_valid_ethereum_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    
    eth_regex = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(eth_regex, address))


def is_valid_amount(amount: str | float | int) -> bool:
    try:
        parsed = float(amount)
        return parsed > 0.0
    except (ValueError, TypeError):
        return False
