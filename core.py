import hashlib
from functools import lru_cache
from typing import Tuple

class WalletProcessor:
    def __init__(self, salt: str = "secure_salt"):
        self.salt = salt

    @lru_cache(maxsize=1024)
    def derive_key(self, input_data: str) -> bytes:
        """Efficient derivation using cached hash results."""
        return hashlib.sha256((input_data + self.salt).encode()).digest()

    def batch_process(self, data_points: Tuple[str, ...]) -> list:
        """Optimized bulk processing with comprehension."""
        return [self.derive_key(dp) for dp in data_points]

    def clear_cache(self) -> None:
        self.derive_key.cache_clear()

    @staticmethod
    def validate_checksum(data: bytes, expected: bytes) -> bool:
        """Constant-time comparison to prevent timing attacks."""
        if len(data) != len(expected):
            return False
        result = 0
        for x, y in zip(data, expected):
            result |= x ^ y
        return result == 0