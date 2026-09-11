import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(current_delay)
                        current_delay *= backoff
            logger.error(f"failed after {retries} attempts")
            raise last_exception
        return wrapper
    return decorator