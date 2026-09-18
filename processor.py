import time
import random
import logging
import urllib.request
import urllib.error
import json
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("wallet_utility.processor")

def retry_network_op(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Operation failed after {retries} attempts: {e}")
                        raise e
                    sleep_time = backoff_factor * (2 ** (attempt - 1)) + random.uniform(0, 0.1)
                    logger.warning(
                        f"Network operation failed: {e}. Retrying in {sleep_time:.2f}s... "
                        f"(Attempt {attempt}/{retries})"
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator

class CryptoNodeProcessor:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @retry_network_op(retries=4, backoff_factor=1.0, exceptions=(ConnectionError, TimeoutError))
    def query_blockchain(self, payload: dict) -> dict:
        req = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            raise ConnectionError(f"Failed to connect to node: {e}") from e
