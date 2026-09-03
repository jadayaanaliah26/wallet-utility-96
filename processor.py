import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Any, Dict, List


@lru_cache(maxsize=2048)
def derive_address_fast(pubkey_bytes: bytes) -> str:
    sha = hashlib.sha256(pubkey_bytes).digest()
    return hashlib.new("ripemd160", sha).hexdigest()


class BatchTransactionProcessor:
    def __init__(self, max_workers: int = 8):
        self.max_workers = max_workers

    def process_payload(self, tx: Dict[str, Any]) -> Dict[str, Any]:
        pubkey = bytes.fromhex(tx["pubkey"])
        sender_address = derive_address_fast(pubkey)
        tx_hash = hashlib.sha256(bytes.fromhex(tx["raw_hex"])).hexdigest()
        return {
            "txid": tx_hash,
            "sender": sender_address,
            "amount": tx["amount"],
            "valid": len(tx_hash) == 64,
        }

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(self.process_payload, transactions))
