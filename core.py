import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Dict, List, Optional


class WalletCore:
    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers

    @staticmethod
    @lru_cache(maxsize=1024)
    def derive_address_hash(pubkey_hex: str, network_prefix: str = "00") -> str:
        raw_bytes = bytes.fromhex(pubkey_hex)
        sha = hashlib.sha256(raw_bytes).digest()
        ripemd = hashlib.new("ripemd160", sha).digest()
        payload = bytes.fromhex(network_prefix) + ripemd
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        return (payload + checksum).hex()

    def process_batch_pubkeys(
        self, pubkeys: List[str], prefix: str = "00"
    ) -> Dict[str, str]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                pk: executor.submit(self.derive_address_hash, pk, prefix)
                for pk in pubkeys
            }
            return {pk: fut.result() for pk, fut in futures.items()}

    @lru_cache(maxsize=512)
    def validate_tx_hash(self, tx_hex: str) -> Optional[str]:
        if not tx_hex or len(tx_hex) % 2 != 0:
            return None
        try:
            raw_tx = bytes.fromhex(tx_hex)
            first_pass = hashlib.sha256(raw_tx).digest()
            return hashlib.sha256(first_pass).hexdigest()
        except ValueError:
            return None
