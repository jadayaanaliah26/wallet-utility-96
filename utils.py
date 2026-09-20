import time
import functools
from typing import Callable, Any, Type

def retry(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

def handle_network_request(func: Callable) -> Callable:
    return retry((ConnectionError, TimeoutError), max_retries=3, delay=2.0)(func)