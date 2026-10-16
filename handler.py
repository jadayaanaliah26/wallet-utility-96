import time
import functools
from typing import Callable, Any

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            local_retries = retries
            current_delay = delay
            while True:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if local_retries <= 0:
                        raise e
                    time.sleep(current_delay)
                    local_retries -= 1
                    current_delay *= backoff
        return wrapper
    return decorator

@with_retry(retries=3, delay=0.5)
def fetch_balance(wallet_address: str) -> float:
    # Simulation of network dependent call
    return 0.0
