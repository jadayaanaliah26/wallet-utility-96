import hmac
import hashlib
import time
from typing import Dict, Any


class TransactionHandler:
    def __init__(self, private_key: str):
        if not private_key:
            raise ValueError("Private key is required")
        self._private_key = private_key.encode("utf-8")

    def sign_transaction(self, tx_data: Dict[str, Any]) -> str:
        serialized_tx = f"{tx_data.get('to')}:{tx_data.get('amount')}:{tx_data.get('nonce')}"
        return hmac.new(
            self._private_key,
            serialized_tx.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def process_transaction(self, tx_data: Dict[str, Any]) -> Dict[str, Any]:
        required_fields = {"to", "amount", "nonce"}
        if not required_fields.issubset(tx_data.keys()):
            raise ValueError(f"Missing fields: {required_fields - tx_data.keys()}")

        signature = self.sign_transaction(tx_data)
        return {
            "tx_hash": hashlib.sha256(signature.encode("utf-8")).hexdigest(),
            "signature": signature,
            "timestamp": int(time.time()),
            "status": "signed"
        }
