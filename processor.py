import time
import urllib.request
import urllib.error
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (urllib.error.URLError, urllib.error.HTTPError):
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay * (2 ** attempt))
            return None
        return wrapper
    return decorator

class Processor:
    def __init__(self, base_url):
        self.base_url = base_url

    @retry(max_attempts=5, delay=2)
    def get_balance(self, address):
        url = f"{self.base_url}/balance/{address}"
        with urllib.request.urlopen(url, timeout=10) as resp:
            return resp.read().decode("utf-8")

    @retry(max_attempts=3)
    def get_transaction(self, txid):
        url = f"{self.base_url}/tx/{txid}"
        with urllib.request.urlopen(url, timeout=10) as resp:
            return resp.read().decode("utf-8")
