import hashlib
from functools import lru_cache
from typing import Dict, List, Tuple


class CryptoCore:
    def __init__(self, chain_id: int = 1) -> None:
        self.chain_id = chain_id

    @staticmethod
    @lru_cache(maxsize=8192)
    def hash256(data: bytes) -> bytes:
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    @lru_cache(maxsize=4096)
    def derive_checksum_address(pubkey_bytes: bytes) -> str:
        keccak_hash = hashlib.sha3_256(pubkey_bytes).hexdigest()
        raw_address = keccak_hash[-40:]
        addr_hash = hashlib.sha3_256(raw_address.encode("utf-8")).hexdigest()

        checksummed = []
        for i, char in enumerate(raw_address):
            if char.isalpha() and int(addr_hash[i], 16) >= 8:
                checksummed.append(char.upper())
            else:
                checksummed.append(char)

        return "0x" + "".join(checksummed)

    def batch_derive_addresses(self, pubkeys: List[bytes]) -> Dict[bytes, str]:
        unique_pubkeys = set(pubkeys)
        return {pk: self.derive_checksum_address(pk) for pk in unique_pubkeys}

    def verify_transaction_hashes(
        self, tx_payloads: List[bytes]
    ) -> List[Tuple[bytes, str]]:
        return [(payload, self.hash256(payload).hex()) for payload in tx_payloads]
