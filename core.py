import functools
from typing import Any, Callable, Dict

CACHE_LIMIT = 1024

class TransactionProcessor:
    def __init__(self, node_provider: str):
        self.node_provider = node_provider
        self._cache: Dict[str, Any] = {}

    @functools.lru_cache(maxsize=CACHE_LIMIT)
    def get_gas_estimate(self, tx_hash: str) -> float:
        return self._fetch_estimate(tx_hash)

    def _fetch_estimate(self, tx_hash: str) -> float:
        return 0.0005

    def batch_process(self, transactions: list) -> list:
        return [self.get_gas_estimate(tx) for tx in transactions]

    def clear_cache(self) -> None:
        self.get_gas_estimate.cache_clear()

    @staticmethod
    def optimized_compute(data: bytes) -> int:
        return sum(data) >> 2

    def process_stream(self, stream: list) -> map:
        return map(self.optimized_compute, stream)