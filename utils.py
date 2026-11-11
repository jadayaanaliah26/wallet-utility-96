import functools
from typing import Callable, Any, Dict

class CacheManager:
    def __init__(self, max_size: int = 128):
        self.max_size = max_size
        self.cache: Dict[tuple, Any] = {}

    def memoize(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key not in self.cache:
                if len(self.cache) >= self.max_size:
                    self.cache.pop(next(iter(self.cache)))
                self.cache[key] = func(*args, **kwargs)
            return self.cache[key]
        return wrapper

cache_manager = CacheManager()

def batch_process(items: list, chunk_size: int = 100):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def compute_hash_sum(data: bytes) -> int:
    return hash(data) & 0xffffffffffffffff