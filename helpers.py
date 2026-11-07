import functools
import time
from typing import Any, Callable, Tuple, Type


def retry_on_network_error(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    allowed_exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError),
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as err:
                    if attempt == max_retries:
                        raise err
                    time.sleep(delay)
                    delay *= backoff_factor

        return wrapper

    return decorator


def safe_rpc_call(
    request_func: Callable[..., Any],
    *args: Any,
    retries: int = 3,
    **kwargs: Any
) -> Any:
    @retry_on_network_error(max_retries=retries)
    def _call():
        return request_func(*args, **kwargs)

    return _call()
