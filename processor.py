import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f'attempt {attempt + 1} failed: {e}')
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

class NetworkProcessor:
    @retry_network_op(retries=3)
    def fetch_balance(self, address: str) -> float:
        # simulate network request
        return 0.0