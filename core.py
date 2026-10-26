import hashlib
from functools import lru_cache
from typing import Dict, List, Tuple


class WalletCore:
    def __init__(self, seed: bytes) -> None:
        self._seed = seed

    @staticmethod
    @lru_cache(maxsize=1024)
    def derive_key(seed: bytes, index: int) -> bytes:
        hasher = hashlib.sha256()
        hasher.update(seed)
        hasher.update(index.to_bytes(4, byteorder="big"))
        return hashlib.pbkdf2_hmac("sha256", hasher.digest(), b"salt", 1000)

    @staticmethod
    @lru_cache(maxsize=1024)
    def generate_address(public_key: bytes) -> str:
        sha = hashlib.sha256(public_key).digest()
        ripemd = hashlib.new("ripemd160", sha).hexdigest()
        return f"0x{ripemd}"

    def batch_derive_addresses(self, start_index: int, count: int) -> List[Dict[str, str]]:
        results = []
        for i in range(start_index, start_index + count):
            private_key = self.derive_key(self._seed, i)
            public_key = hashlib.sha256(private_key).digest()
            address = self.generate_address(public_key)
            results.append({"index": str(i), "address": address})
        return results

    def verify_batch_signatures(self, items: List[Tuple[bytes, bytes, str]]) -> List[bool]:
        cached_verifications: Dict[Tuple[bytes, bytes], bool] = {}
        results = []
        for msg, sig, expected_addr in items:
            cache_key = (msg, sig)
            if cache_key not in cached_verifications:
                derived_hash = hashlib.sha256(msg + sig).digest()
                addr = self.generate_address(derived_hash)
                cached_verifications[cache_key] = addr == expected_addr
            results.append(cached_verifications[cache_key])
        return results
