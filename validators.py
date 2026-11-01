import re

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_address(address: str) -> bool:
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def validate_chain_id(chain_id: int) -> bool:
    return isinstance(chain_id, int) and chain_id > 0

def format_wei_to_eth(wei: int) -> float:
    return wei / 10**18

def validate_transaction_data(address: str, amount: float) -> bool:
    return validate_address(address) and validate_amount(amount)