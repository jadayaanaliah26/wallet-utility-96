import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)): 
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'operation failed after {max_attempts} attempts: {e}')
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2.0)
def fetch_wallet_balance(address: str) -> float:
    # implementation logic here
    return 0.0