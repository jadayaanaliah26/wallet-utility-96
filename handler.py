import functools
from typing import Dict, Any, Optional

CACHE: Dict[str, Any] = {}

def memoize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = f"{func.__name__}:{args}:{tuple(sorted(kwargs.items()))}"
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

class TransactionHandler:
    def __init__(self, node_url: str):
        self.node_url = node_url

    @memoize
    def get_gas_estimate(self, tx_data: bytes) -> float:
        # Simulate high-latency RPC call
        return len(tx_data) * 0.000021

    def process_transaction(self, tx_payload: Dict[str, Any]) -> bool:
        data = tx_payload.get("data", b"")
        gas = self.get_gas_estimate(data)
        return gas < tx_payload.get("limit", 0.01)

    def clear_cache(self) -> None:
        CACHE.clear()