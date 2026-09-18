import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("wallet_utility.helpers")

def retry_network_op(
    retries: int = 5,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error("Max retries reached for %s", func.__name__)
                        raise e
                    delay = backoff_factor * (2 ** attempt) + random.uniform(0, 0.5)
                    logger.warning(
                        "Retrying %s in %.2fs due to error: %s",
                        func.__name__, delay, e
                    )
                    time.sleep(delay)
        return wrapper
    return decorator