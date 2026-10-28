import re
from typing import Any, Dict, List, Optional


class CryptoDataProcessor:
    @staticmethod
    def satoshi_to_btc(satoshis: int) -> float:
        if not isinstance(satoshis, int) or satoshis < 0:
            raise ValueError("Satoshis must be a non-negative integer")
        return satoshis / 100_000_000.0

    @staticmethod
    def wei_to_eth(wei: int) -> float:
        if not isinstance(wei, int) or wei < 0:
            raise ValueError("Wei must be a non-negative integer")
        return wei / 10**18

    @staticmethod
    def normalize_address(address: str, chain: str = "btc") -> str:
        address = address.strip()
        if chain.lower() in ("btc", "bitcoin"):
            if not re.match(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$", address):
                raise ValueError("Invalid Bitcoin address format")
            return address
        elif chain.lower() in ("eth", "ethereum"):
            if not re.match(r"^0x[a-fA-F0-9]{40}$", address):
                raise ValueError("Invalid Ethereum address format")
            return address.lower()
        raise ValueError(f"Unsupported chain: {chain}")

    @classmethod
    def parse_transaction_batch(
        cls, raw_txs: List[Dict[str, Any]], chain: str = "eth"
    ) -> List[Dict[str, Any]]:
        processed = []
        for tx in raw_txs:
            tx_id = tx.get("hash") or tx.get("txid")
            amount_raw = tx.get("value", 0)
            amount = (
                cls.wei_to_eth(amount_raw)
                if chain.lower() == "eth"
                else cls.satoshi_to_btc(amount_raw)
            )
            processed.append(
                {
                    "tx_id": str(tx_id).lower() if tx_id else None,
                    "from_address": cls.normalize_address(tx.get("from", ""), chain)
                    if tx.get("from")
                    else None,
                    "to_address": cls.normalize_address(tx.get("to", ""), chain)
                    if tx.get("to")
                    else None,
                    "amount": amount,
                    "chain": chain.lower(),
                }
            )
        return processed
