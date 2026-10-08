import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"operation failed after {max_retries} attempts")
                        raise e
                    time.sleep(delay * (2 ** (attempts - 1)))
            return None
        return wrapper
    return decorator

@retry_network_operation(max_retries=3)
def fetch_balance(address: str) -> dict:
    # Simulated network call
    return {"address": address, "balance": 0.0}

def process_transaction(tx_data: dict) -> bool:
    try:
        return bool(fetch_balance(tx_data.get("from")))
    except Exception:
        return False