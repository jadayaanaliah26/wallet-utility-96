from functools import lru_cache
from typing import Dict, Any, List
import hashlib

class TransactionProcessor:
    def __init__(self, fee_rate: float = 0.001):
        self.fee_rate = fee_rate
        self._cache_hits = 0

    @lru_cache(maxsize=1024)
    def calculate_hash(self, tx_data: str) -> str:
        self._cache_hits += 1
        return hashlib.sha256(tx_data.encode('utf-8')).hexdigest()

    def batch_process(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        for tx in transactions:
            raw_payload = f"{tx.get('sender', '')}:{tx.get('recipient', '')}:{tx.get('amount', 0.0)}"
            tx_hash = self.calculate_hash(raw_payload)
            fee = float(tx.get('amount', 0.0)) * self.fee_rate
            
            processed_tx = {
                'id': tx_hash,
                'sender': tx.get('sender'),
                'recipient': tx.get('recipient'),
                'amount': tx.get('amount'),
                'fee': fee,
                'status': 'optimized'
            }
            processed.append(processed_tx)
        return processed

    def get_optimization_stats(self) -> Dict[str, int]:
        cache_info = self.calculate_hash.cache_info()
        return {
            'hits': cache_info.hits,
            'misses': cache_info.misses,
            'maxsize': cache_info.maxsize,
            'currsize': cache_info.currsize
        }
