import functools
from typing import Callable, Any, Dict

CACHE: Dict[str, Any] = {}

class CryptoCache:
    @staticmethod
    def memoize(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
            if key not in CACHE:
                CACHE[key] = func(*args, **kwargs)
            return CACHE[key]
        return wrapper

@CryptoCache.memoize
def derive_address_checksum(pubkey: bytes) -> str:
    import hashlib
    return hashlib.sha256(pubkey).hexdigest()[:8]

def batch_process_signatures(signatures: list[bytes]) -> list[str]:
    return [derive_address_checksum(s) for s in signatures]

def clear_cache() -> None:
    CACHE.clear()