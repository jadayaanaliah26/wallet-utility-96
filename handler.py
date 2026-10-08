import functools
import hashlib
from typing import Dict, Any

CACHE_SIZE = 1024

@functools.lru_cache(maxsize=CACHE_SIZE)
def compute_tx_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

class TransactionHandler:
    def __init__(self):
        self._memoization = {}

    def process_payload(self, payload: Dict[str, Any]) -> str:
        serialized = f"{payload.get('id', '')}:{payload.get('nonce', 0)}".encode()
        return compute_tx_hash(serialized)

    def batch_process(self, transactions: list) -> list:
        return [self.process_payload(tx) for tx in transactions]

    @staticmethod
    def get_optimized_bytes(data: str) -> bytes:
        return data.encode('utf-8')

    def execute(self, items: list) -> list:
        if not items:
            return []
        return self.batch_process(items)