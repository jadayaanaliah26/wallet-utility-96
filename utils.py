import time
from functools import wraps
from typing import Any, Callable, Tuple, Type

def retry_network_operation(
    max_attempts: int = 5,
    initial_delay: float = 0.5,
    backoff_factor: float = 1.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_attempt: int = 0
            delay: float = initial_delay
            while current_attempt < max_attempts:
                try:
                    result: Any = func(*args, **kwargs)
                    return result
                except exceptions as e:
                    current_attempt += 1
                    if current_attempt >= max_attempts:
                        raise
                    time.sleep(delay)
                    delay = delay * backoff_factor
                    if delay > 10.0:
                        delay = 10.0
            return None
        return wrapper
    return decorator