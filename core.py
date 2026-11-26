import hashlib
import hmac
import json
from typing import Any, Dict

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_amount(amount: float, decimals: int = 8) -> str:
    return f"{amount:.{decimals}f}"

def sanitize_request(data: Dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(',', ':'))

def validate_address(address: str, prefix: str = '0x') -> bool:
    if not address.startswith(prefix):
        return False
    return len(address) == 42

def parse_fee(base_fee: float, gas_multiplier: float) -> float:
    return round(base_fee * gas_multiplier, 8)