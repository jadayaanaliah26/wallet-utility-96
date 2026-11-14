import hashlib
import hmac
from functools import lru_cache
from typing import Dict, List, Tuple


class WalletCore:
    __slots__ = ("master_key", "_derivation_cache")

    def __init__(self, master_key: bytes):
        self.master_key = master_key
        self._derivation_cache: Dict[bytes, bytes] = {}

    @staticmethod
    @lru_cache(maxsize=2048)
    def hash256(data: bytes) -> bytes:
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    @lru_cache(maxsize=2048)
    def hash160(data: bytes) -> bytes:
        sha = hashlib.sha256(data).digest()
        return hashlib.sha256(sha).digest()[:20]

    def derive_key(self, path_index: int, chain_code: bytes) -> Tuple[bytes, bytes]:
        data = path_index.to_bytes(4, byteorder="big") + chain_code
        if data in self._derivation_cache:
            derived = self._derivation_cache[data]
        else:
            derived = hmac.new(self.master_key, data, hashlib.sha512).digest()
            self._derivation_cache[data] = derived
        return derived[:32], derived[32:]

    def batch_hash_pubkeys(self, pubkeys: List[bytes]) -> List[bytes]:
        return [self.hash160(pk) for pk in pubkeys]

    def process_transaction_batch(self, tx_payloads: List[bytes]) -> List[bytes]:
        return [self.hash256(tx) for tx in tx_payloads]

    def purge_caches(self) -> None:
        self._derivation_cache.clear()
        self.hash256.cache_clear()
        self.hash160.cache_clear()
