import hashlib
import hmac
from typing import Tuple


class WalletCore:
    """Core cryptographic operations for hierarchical deterministic wallets."""

    def __init__(self, seed: bytes) -> None:
        """Initialize the wallet core with a master seed."""
        self.seed = seed

    def generate_master_keys(self) -> Tuple[bytes, bytes]:
        """Derive the master private key and chain code from seed.

        Returns:
            A tuple of (private_key, chain_code).
        """
        identifier = b"Bitcoin seed"
        digest = hmac.new(identifier, self.seed, hashlib.sha512).digest()
        return digest[:32], digest[32:]

    def derive_hardened_child(
        self, parent_key: bytes, chain_code: bytes, index: int
    ) -> Tuple[bytes, bytes]:
        """Derive a hardened child key from parent key and chain code.

        Args:
            parent_key: 32-byte parent private key.
            chain_code: 32-byte parent chain code.
            index: Child index (usually >= 0x80000000).

        Returns:
            A tuple of (child_private_key, child_chain_code).
        """
        data = bytes([0]) + parent_key + index.to_bytes(4, byteorder="big")
        digest = hmac.new(chain_code, data, hashlib.sha512).digest()
        return digest[:32], digest[32:]
