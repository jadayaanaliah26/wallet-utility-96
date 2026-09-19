from functools import lru_cache
from typing import Dict, Optional
import hashlib

@lru_cache(maxsize=1024)
def derive_address_hash(public_key: str) -> str:
    return hashlib.sha256(public_key.encode()).hexdigest()

def batch_process_signatures(signatures: list, salt: str) -> Dict[str, str]:
    return {sig: hashlib.sha256((sig + salt).encode()).hexdigest() for sig in signatures}

class DataBuffer:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self._storage: list = []

    def append(self, item: str) -> None:
        if len(self._storage) >= self.capacity:
            self._storage.pop(0)
        self._storage.append(item)

    def get_snapshot(self) -> tuple:
        return tuple(self._storage)

def compute_fee_tier(amount: float) -> int:
    if amount < 1.0:
        return 0
    if amount < 10.0:
        return 1
    return 2