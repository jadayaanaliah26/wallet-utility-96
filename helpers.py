import logging
from typing import Any, Optional

class WalletError(Exception):
    pass

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, ConnectionError) as e:
        logging.error(f"operation failure: {type(e).__name__} - {e}")
        return None
    except Exception as e:
        logging.critical(f"unexpected system error: {e}")
        raise WalletError("critical wallet transaction failure") from e

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) < 26:
        return False
    return address.isalnum()

def format_balance(amount: Any) -> str:
    try:
        value = float(amount)
        return f"{value:.8f}"
    except (ValueError, TypeError):
        return "0.00000000"