import hashlib
from functools import lru_cache
from typing import Dict, List

class TransactionProcessor:
    def __init__(self, cache_size: int = 1024):
        self.cache_size = cache_size

    @lru_cache(maxsize=1024)
    def _hash_tx(self, tx_data: bytes) -> str:
        return hashlib.sha256(tx_data).hexdigest()

    def batch_process(self, transactions: List[bytes]) -> List[str]:
        return [self._hash_tx(tx) for tx in transactions]

    def compute_merkle_root(self, hashes: List[str]) -> str:
        if not hashes:
            return ""
        
        nodes = hashes
        while len(nodes) > 1:
            if len(nodes) % 2 != 0:
                nodes.append(nodes[-1])
            
            nodes = [
                hashlib.sha256((nodes[i] + nodes[i+1]).encode()).hexdigest()
                for i in range(0, len(nodes), 2)
            ]
        return nodes[0]

    def validate_batch(self, batch_map: Dict[str, bytes]) -> bool:
        return all(
            self._hash_tx(data) == expected 
            for expected, data in batch_map.items()
        )