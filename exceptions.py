class WalletError(Exception):
    """Base exception for wallet-utility-96"""


class InsufficientFundsError(WalletError):
    """Raised when transaction amount exceeds balance"""


class InvalidAddressError(WalletError):
    """Raised for malformed crypto addresses"""


class NetworkTimeoutError(WalletError):
    """Raised when node connectivity fails"""


class SigningError(WalletError):
    """Raised when transaction signature fails"""


def handle_wallet_exception(e: Exception) -> dict:
    if isinstance(e, InsufficientFundsError):
        return {"status": "error", "code": 402, "message": str(e)}
    if isinstance(e, InvalidAddressError):
        return {"status": "error", "code": 400, "message": str(e)}
    if isinstance(e, NetworkTimeoutError):
        return {"status": "error", "code": 503, "message": "node offline"}
    if isinstance(e, SigningError):
        return {"status": "error", "code": 403, "message": "invalid credentials"}
    return {"status": "error", "code": 500, "message": "internal system failure"}