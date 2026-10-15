import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry(exceptions: Tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"attempt {attempt + 1} failed: {e}. retrying...")
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator