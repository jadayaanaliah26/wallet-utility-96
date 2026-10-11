import hashlib
from functools import lru_cache
from typing import List, Dict, Any


class WalletCore:
    def __init__(self, network: str = "mainnet"):
        self.network = network

    @staticmethod
    @lru_cache(maxsize=1024)
    def derive_address(public_key_hex: str) -> str:
        pub_bytes = bytes.fromhex(public_key_hex)
        sha = hashlib.sha256(pub_bytes).digest()
        ripemd = hashlib.new("ripemd160", sha).digest()
        return ripemd.hex()

    def batch_derive_addresses(self, public_keys: List[str]) -> Dict[str, str]:
        return {pk: self.derive_address(pk) for pk in public_keys}

    @staticmethod
    @lru_cache(maxsize=2048)
    def verify_tx_hash(tx_payload: bytes) -> str:
        return hashlib.sha256(hashlib.sha256(tx_payload).digest()).hexdigest()

    def process_transaction_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = []
        for tx in transactions:
            raw_payload = tx.get("payload", b"")
            if isinstance(raw_payload, str):
                raw_payload = raw_payload.encode("utf-8")
            tx_hash = self.verify_tx_hash(raw_payload)
            results.append({"tx_id": tx.get("id"), "hash": tx_hash, "status": "verified"})
        return results
