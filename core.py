import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Dict, List, Tuple


class WalletCore:
    def __init__(self, pool_size: int = 8) -> None:
        self.pool_size = pool_size

    @staticmethod
    @lru_cache(maxsize=4096)
    def fast_hash(data: bytes) -> str:
        first = hashlib.sha256(data).digest()
        return hashlib.sha256(first).hexdigest()

    @classmethod
    def derive_child_key(cls, parent_key: bytes, index: int) -> bytes:
        data = parent_key + index.to_bytes(4, byteorder="big")
        return hashlib.pbkdf2_hmac("sha256", data, b"wallet_salt", 1000)

    def parallel_derive_batch(self, master_seed: bytes, indices: List[int]) -> Dict[int, str]:
        def process_index(idx: int) -> Tuple[int, str]:
            child = self.derive_child_key(master_seed, idx)
            return idx, self.fast_hash(child)

        with ThreadPoolExecutor(max_workers=self.pool_size) as executor:
            results = executor.map(process_index, indices)
        return dict(results)

    @lru_cache(maxsize=1024)
    def verify_checksum(self, payload_hex: str, expected_checksum: str) -> bool:
        computed = self.fast_hash(bytes.fromhex(payload_hex))[:8]
        return computed == expected_checksum
