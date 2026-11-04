from typing import Dict, Any, List, Optional
import hashlib
import json


class TransactionProcessor:
    """Processes and validates raw cryptocurrency transaction payloads."""

    def __init__(self, chain_id: int = 1) -> None:
        self.chain_id = chain_id

    def normalize_address(self, address: str) -> str:
        """Formats address to standard lowercase representation.

        Args:
            address: Raw wallet address string.

        Returns:
            Normalized address string.
        """
        address = address.strip()
        if address.startswith("0x"):
            return address.lower()
        return address

    def calculate_tx_hash(self, tx_data: Dict[str, Any]) -> str:
        """Generates SHA-256 hash representation of transaction data.

        Args:
            tx_data: Dictionary containing transaction details.

        Returns:
            Hexadecimal hash string.
        """
        serialized = json.dumps(tx_data, sort_keys=True).encode("utf-8")
        return hashlib.sha256(serialized).hexdigest()

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Processes a list of raw transaction objects.

        Args:
            transactions: List of raw transaction dictionaries.

        Returns:
            List of processed transactions with calculated hashes.
        """
        processed: List[Dict[str, Any]] = []
        for tx in transactions:
            item = tx.copy()
            if "from" in item and isinstance(item["from"], str):
                item["from"] = self.normalize_address(item["from"])
            if "to" in item and isinstance(item["to"], str):
                item["to"] = self.normalize_address(item["to"])
            item["chain_id"] = self.chain_id
            item["tx_hash"] = self.calculate_tx_hash(item)
            processed.append(item)
        return processed
