import hashlib
from functools import lru_cache
from typing import List, Tuple


class WalletCore:
    def __init__(self, seed: bytes):
        self.seed = seed

    @staticmethod
    @lru_cache(maxsize=4096)
    def _hash160(pub_key: bytes) -> bytes:
        sha = hashlib.sha256(pub_key).digest()
        rip = hashlib.new("ripemd160")
        rip.update(sha)
        return rip.digest()

    @lru_cache(maxsize=2048)
    def derive_child_key(self, parent_key: bytes, index: int) -> bytes:
        data = parent_key + index.to_bytes(4, byteorder="big")
        return hashlib.pbkdf2_hmac("sha512", self.seed, data, iterations=100)

    def batch_derive_addresses(
        self, parent_key: bytes, start_idx: int, count: int
    ) -> List[Tuple[int, str]]:
        results = []
        for i in range(start_idx, start_idx + count):
            child = self.derive_child_key(parent_key, i)
            h160 = self._hash160(child)
            results.append((i, h160.hex()))
        return results

    def clear_cache(self) -> None:
        self._hash160.cache_clear()
        self.derive_child_key.cache_clear()
