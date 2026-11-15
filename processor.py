import hashlib
from typing import List, Dict, Any

class WalletProcessor:
    def __init__(self, network: str = 'mainnet'):
        self.network = network

    def validate_address(self, address: str) -> bool:
        return len(address) == 42 and address.startswith('0x')

    def sanitize_transaction(self, tx: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'hash': hashlib.sha256(str(tx).encode()).hexdigest(),
            'amount': float(tx.get('amount', 0)),
            'valid': self.validate_address(tx.get('to', ''))
        }

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [self.sanitize_transaction(tx) for tx in transactions]

def initialize_processor(network: str) -> WalletProcessor:
    return WalletProcessor(network)