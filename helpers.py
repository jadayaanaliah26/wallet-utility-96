import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class WalletError(Exception):
    pass

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return address.startswith('0x')

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid input for {func.__name__}: {e}")
        return None
    except ConnectionError as e:
        logger.critical(f"Network failure in {func.__name__}: {e}")
        raise WalletError("Remote node unreachable") from e
    except Exception as e:
        logger.exception(f"Unexpected failure in {func.__name__}: {e}")
        return None

def format_wei(value: Any) -> int:
    try:
        val = int(value)
        if val < 0:
            raise ValueError("Negative balance provided")
        return val
    except (ValueError, TypeError):
        return 0