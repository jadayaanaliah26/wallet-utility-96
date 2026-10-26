import hashlib
import hmac
from typing import Optional

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def validate_address(address: str, chain: str) -> bool:
    if chain == 'eth':
        return len(address) == 42 and address.startswith('0x')
    if chain == 'btc':
        return 26 <= len(address) <= 35
    return False

def format_wei(amount: int) -> float:
    return float(amount) / 10**18

def sanitize_input(data: Optional[str]) -> str:
    if not data:
        return ''
    return data.strip().lower()

class WalletError(Exception):
    pass

def get_error_message(error: Exception) -> str:
    return f'wallet-utility-96 error: {str(error)}'