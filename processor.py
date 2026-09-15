import hashlib
import json
from typing import Dict, Any, List

class TransactionProcessor:
    def __init__(self, chain_id: int = 1):
        self.chain_id = chain_id

    def compute_tx_hash(self, tx_data: Dict[str, Any]) -> str:
        serialized = json.dumps(tx_data, sort_keys=True).encode("utf-8")
        return hashlib.sha256(serialized).hexdigest()

    def validate_structure(self, tx_data: Dict[str, Any]) -> bool:
        required_fields = {"sender", "recipient", "amount", "nonce"}
        return all(field in tx_data for field in required_fields)

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        for tx in transactions:
            if not self.validate_structure(tx):
                continue
            tx_hash = self.compute_tx_hash(tx)
            processed_tx = {
                **tx,
                "tx_hash": tx_hash,
                "chain_id": self.chain_id,
                "status": "ready"
            }
            processed.append(processed_tx)
        return processed