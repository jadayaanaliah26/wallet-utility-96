import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(f"Operation failed after {max_retries} attempts: {exc}")
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed ({exc}). "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator
