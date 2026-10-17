import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation {func.__name__} failed after {max_retries} attempts: {err}"
                        )
                        raise
                    sleep_time = delay * (1 + random.random()) if jitter else delay
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for {func.__name__}: {err}. Retrying in {sleep_time:.2f}s"
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper

    return decorator
