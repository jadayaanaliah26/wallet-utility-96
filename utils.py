from typing import Dict, Any, Optional
import hashlib
import hmac

def validate_address(address: str, chain: str) -> bool:
    if not address or len(address) < 26:
        return False
    return address.isalnum()

def calculate_checksum(data: str, secret: str) -> str:
    return hmac.new(
        secret.encode(),
        data.encode(),
        hashlib.sha256
    ).hexdigest()

def format_amount(value: float, precision: int = 8) -> float:
    return round(value, precision)

def sanitize_transaction(tx_data: Dict[str, Any]) -> Dict[str, Any]:
    required = {'sender', 'receiver', 'amount'}
    if not all(key in tx_data for key in required):
        raise ValueError('Missing transaction fields')
    return {
        'sender': str(tx_data['sender']),
        'receiver': str(tx_data['receiver']),
        'amount': float(tx_data['amount'])
    }

def derive_asset_id(symbol: str, chain_id: int) -> str:
    payload = f"{symbol.upper()}:{chain_id}"
    return hashlib.sha256(payload.encode()).hexdigest()[:16]