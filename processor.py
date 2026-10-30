import time
import functools
from typing import Callable, Any, Type

def retry_operation(retries: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=0.5)
def fetch_balance(address: str) -> float:
    # Simulated network call
    return 0.0

class NetworkProcessor:
    @retry_operation(retries=5)
    def broadcast_transaction(self, tx_data: dict) -> str:
        return "success"
