import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Dict, List, Union


class TransactionProcessor:
    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers

    @staticmethod
    @lru_cache(maxsize=4096)
    def hash_payload(payload: bytes) -> str:
        first_hash = hashlib.sha256(payload).digest()
        return hashlib.sha256(first_hash).hexdigest()

    def serialize_tx(self, tx: Dict[str, Union[str, int]]) -> bytes:
        return f"{tx['from']}:{tx['to']}:{tx['value']}:{tx['nonce']}".encode("utf-8")

    def process_single(self, tx: Dict[str, Union[str, int]]) -> str:
        serialized = self.serialize_tx(tx)
        return self.hash_payload(serialized)

    def process_batch(self, transactions: List[Dict[str, Union[str, int]]]) -> List[str]:
        if len(transactions) < 10:
            return [self.process_single(tx) for tx in transactions]

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(self.process_single, transactions))
