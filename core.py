import hashlib
import re
from typing import Any, Dict, Union


class CryptoDataProcessor:
    ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
    BTC_ADDRESS_PATTERN = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$")

    @staticmethod
    def to_wei(amount: Union[int, float, str], decimals: int = 18) -> int:
        return int(float(amount) * (10**decimals))

    @staticmethod
    def from_wei(amount_wei: int, decimals: int = 18) -> float:
        return amount_wei / (10**decimals)

    @classmethod
    def validate_address(cls, address: str, chain: str = "eth") -> bool:
        if not isinstance(address, str):
            return False
        chain = chain.lower()
        if chain in ("eth", "ethereum"):
            return bool(cls.ETH_ADDRESS_PATTERN.match(address))
        elif chain in ("btc", "bitcoin"):
            return bool(cls.BTC_ADDRESS_PATTERN.match(address))
        return False

    @staticmethod
    def format_transaction_payload(tx_data: Dict[str, Any]) -> Dict[str, Any]:
        required_keys = {"to", "value", "chain"}
        missing = required_keys - set(tx_data.keys())
        if missing:
            raise ValueError(f"Missing required keys: {missing}")

        return {
            "to": str(tx_data["to"]).strip(),
            "value_wei": int(tx_data["value"]),
            "chain": str(tx_data["chain"]).lower(),
            "nonce": int(tx_data.get("nonce", 0)),
            "gas_limit": int(tx_data.get("gas_limit", 21000)),
            "data": str(tx_data.get("data", "0x")),
        }

    @staticmethod
    def compute_payload_hash(payload: Dict[str, Any]) -> str:
        raw = f"{payload.get('to')}:{payload.get('value_wei')}:{payload.get('nonce')}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
