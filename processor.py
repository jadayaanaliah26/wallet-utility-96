from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
import hashlib
from typing import Any, Dict, List


class BatchTransactionProcessor:
    def __init__(self, max_workers: int = 8) -> None:
        self.max_workers = max_workers

    @staticmethod
    @lru_cache(maxsize=8192)
    def compute_tx_hash(payload: bytes) -> str:
        return hashlib.blake2b(payload, digest_size=32).hexdigest()

    def _process_single_tx(self, tx: Dict[str, Any]) -> Dict[str, Any]:
        raw_payload = f"{tx['sender']}:{tx['recipient']}:{tx['amount']}:{tx['nonce']}".encode()
        tx_hash = self.compute_tx_hash(raw_payload)
        is_valid = tx['sender'].startswith('0x') and tx['recipient'].startswith('0x')
        return {
            "tx_id": tx["tx_id"],
            "hash": tx_hash,
            "valid": is_valid,
            "fee": tx.get("fee", 0)
        }

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not transactions:
            return []
        if len(transactions) < 16:
            return [self._process_single_tx(tx) for tx in transactions]

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(self._process_single_tx, transactions))
