import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)


class NetworkError(Exception):
    """Raised when a crypto node network call fails after retries."""
    pass


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Decorator to retry network calls with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = backoff_factor
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(f"Operation failed after {max_retries} attempts: {err}")
                        raise NetworkError(f"Failed to execute {func.__name__}") from err
                    
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for {func.__name__}: {err}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
                    delay *= 2
        return wrapper
    return decorator


class NodeClient:
    def __init__(self, rpc_url: str):
        self.rpc_url = rpc_url

    @retry_network_op(max_retries=3, backoff_factor=0.2, exceptions=(ConnectionError, TimeoutError))
    def send_rpc_request(self, method: str, params: list) -> dict:
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
        return {"status": "success", "result": payload}
