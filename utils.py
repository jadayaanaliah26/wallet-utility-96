from decimal import Decimal
from typing import Any, Dict, Union


def to_satoshi(amount: Union[str, Decimal]) -> int:
    """Convert a given amount to satoshis."""
    return int(Decimal(amount) * 1_000_000)


def from_satoshi(satoshis: int) -> Decimal:
    """Convert satoshis back to the original amount."""
    return Decimal(satoshis) / Decimal(1_000_000)


def calculate_fee(transaction_amount: Decimal, fee_rate: Decimal) -> Decimal:
    """Calculate the transaction fee based on the amount and fee rate."""
    return transaction_amount * fee_rate


def validate_address(address: str) -> bool:
    """Validate a cryptocurrency address format."""
    return len(address) in {34, 42}  # Example for Bitcoin


def get_balance(data: Dict[str, Any]) -> Decimal:
    """Extract and return balance from data dictionary."""
    return Decimal(data.get('balance', '0'))
