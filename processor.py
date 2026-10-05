import time
import functools
import requests
from typing import Callable, Any

def retry(attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            current_delay = delay
            while retries < attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError):
                    retries += 1
                    if retries >= attempts:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(attempts=3)
def fetch_balance(address: str) -> dict:
    response = requests.get(f"https://api.crypto.example/v1/wallet/{address}", timeout=5)
    response.raise_for_status()
    return response.json()