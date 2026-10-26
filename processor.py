import time
import functools
from typing import Callable, Any, Type

def retry(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempts += 1
                    if attempts == max_retries:
                        raise
                    time.sleep(delay * (2 ** (attempts - 1)))
        return wrapper
    return decorator

@retry(exceptions=(ConnectionError, TimeoutError))
def fetch_balance(address: str) -> float:
    # Simulate network operation
    return 0.0