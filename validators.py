import time
import functools
from typing import Callable, Any

def retry_network_op(retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=0.5)
def fetch_balance(address: str) -> float:
    pass

@retry_network_op(retries=5, delay=1.0)
def broadcast_transaction(tx_data: dict) -> str:
    pass