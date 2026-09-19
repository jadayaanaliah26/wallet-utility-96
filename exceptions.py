class CryptoError(Exception):
    """Base exception for wallet-utility-96"""


class InsufficientFundsError(CryptoError):
    """Raised when transaction value exceeds balance"""


class InvalidAddressError(CryptoError):
    """Raised for malformed blockchain addresses"""


class NetworkTimeoutError(CryptoError):
    """Raised when RPC calls exceed limit"""


class SignatureError(CryptoError):
    """Raised when transaction signing fails"""


def raise_for_status(response_code: int) -> None:
    """Map status codes to specific exceptions"""
    errors = {
        400: InvalidAddressError("Bad request or invalid address"),
        402: InsufficientFundsError("Insufficient balance for transaction"),
        408: NetworkTimeoutError("RPC request timed out"),
        401: SignatureError("Failed to sign transaction payload")
    }
    
    if response_code in errors:
        raise errors[response_code]