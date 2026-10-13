import logging
from typing import Optional, Dict, Any

class WalletError(Exception):
    pass

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) < 26:
        return False
    return address.isalnum()

def parse_transaction(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        required = ['sender', 'receiver', 'amount']
        if not all(k in data for k in required):
            raise ValueError("missing transaction fields")
        if float(data['amount']) <= 0:
            raise ValueError("invalid transaction amount")
        return data
    except (ValueError, TypeError, KeyError) as e:
        logging.error(f"transaction parsing failure: {e}")
        return None

def secure_transfer(balance: float, amount: float) -> bool:
    try:
        if amount <= 0:
            raise WalletError("negative transfer amount")
        if amount > balance:
            raise WalletError("insufficient funds")
        return True
    except WalletError as e:
        logging.warning(f"transfer validation failed: {e}")
        return False
    except Exception as e:
        logging.critical(f"unexpected system error: {e}")
        return False