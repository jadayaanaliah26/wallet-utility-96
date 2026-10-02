import hashlib
import hmac
from typing import Dict, Optional

class WalletCore:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret.encode('utf-8')

    def generate_signature(self, payload: str) -> str:
        return hmac.new(
            self.api_secret,
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def format_transaction(self, tx_id: str, amount: float, currency: str) -> Dict:
        return {
            "id": tx_id,
            "amount": float(amount),
            "currency": currency.upper(),
            "verified": True
        }

    def validate_address(self, address: str, network: str) -> bool:
        if network == "ethereum":
            return address.startswith("0x") and len(address) == 42
        if network == "bitcoin":
            return len(address) >= 26 and len(address) <= 35
        return False

    @staticmethod
    def sanitize_amount(value: any) -> float:
        try:
            return round(float(value), 8)
        except (ValueError, TypeError):
            return 0.0