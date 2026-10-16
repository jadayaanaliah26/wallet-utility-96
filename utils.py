import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {retries} attempts: {err}"
                        )
                        raise
                    sleep_time = backoff_factor * (2 ** (attempt - 1))
                    logger.warning(
                        f"Operation '{func.__name__}' failed: {err}. "
                        f"Retrying in {sleep_time:.2f}s (Attempt {attempt}/{retries})"
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator