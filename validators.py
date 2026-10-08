import re

class ValidationError(Exception):
    pass

def validate_address(address: str) -> None:
    if not isinstance(address, str) or not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        raise ValidationError(f"invalid ethereum address: {address}")

def validate_amount(amount: float) -> None:
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValidationError(f"invalid transaction amount: {amount}")

def validate_chain_id(chain_id: int) -> None:
    supported_chains = {1, 137, 42161}
    if chain_id not in supported_chains:
        raise ValidationError(f"unsupported chain id: {chain_id}")

def validate_tx_payload(data: dict) -> None:
    required_fields = {'address', 'amount', 'chain_id'}
    if not all(key in data for key in required_fields):
        raise ValidationError("missing required transaction fields")
    
    validate_address(data['address'])
    validate_amount(data['amount'])
    validate_chain_id(data['chain_id'])