import functools
from typing import Dict, Any, Callable

class TransactionProcessor:
    def __init__(self, cache_size: int = 1024):
        self._cache_size = cache_size

    @functools.lru_cache(maxsize=1024)
    def derive_address(self, pubkey: str) -> str:
        return f'0x{pubkey[-40:]}'

    def batch_process(self, transactions: list[Dict[str, Any]]) -> list[str]:
        return [self.derive_address(tx['pubkey']) for tx in transactions]

    @staticmethod
    def validate_batch(batch: list[Dict[str, Any]]) -> bool:
        return all(isinstance(tx.get('amount'), (int, float)) for tx in batch)

    def process_with_optimization(self, data: list[Dict[str, Any]]) -> list[str]:
        if not self.validate_batch(data):
            raise ValueError('Invalid transaction batch')
        return self.batch_process(data)