import time
from functools import wraps
from typing import Callable, Any

def retry_network_call(max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator