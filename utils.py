import hashlib
import hmac
import json
from typing import Any, Dict

def sign_payload(payload: Dict[str, Any], secret: str) -> str:
    message = json.dumps(payload, sort_keys=True).encode()
    return hmac.new(secret.encode(), message, hashlib.sha256).hexdigest()

def format_amount(amount: float, decimals: int = 8) -> str:
    return f"{amount:.{decimals}f}".rstrip('0').rstrip('.')

def validate_address(address: str, prefix: str = '0x') -> bool:
    if not address.startswith(prefix):
        return False
    return len(address) == 42 and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def parse_hex(hex_str: str) -> int:
    return int(hex_str, 16)

def sanitize_currency(symbol: str) -> str:
    return symbol.strip().upper()

if __name__ == "__main__":
    data = {"amount": 1.23456789, "currency": "btc"}
    print(format_amount(data["amount"]))
    print(validate_address("0x71C7656EC7ab88b098defB751B7401B5f6d8976F"))