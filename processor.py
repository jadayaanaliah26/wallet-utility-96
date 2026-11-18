import json
from typing import Dict, Any, List

class WalletProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def sanitize_transaction(self, tx: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "hash": tx.get("hash"),
            "amount": float(tx.get("value", 0)),
            "recipient": tx.get("to"),
            "status": "processed"
        }

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [self.sanitize_transaction(tx) for tx in transactions]

    @staticmethod
    def format_output(data: Any) -> str:
        return json.dumps(data, indent=2)

if __name__ == "__main__":
    processor = WalletProcessor({"network": "mainnet"})
    sample_txs = [{"hash": "0x123", "value": "0.5", "to": "0xabc"}]
    print(processor.format_output(processor.process_batch(sample_txs)))