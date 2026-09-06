class WalletError(Exception):
    """Base exception for wallet-utility-96"""

class InsufficientFundsError(WalletError):
    """Raised when balance is too low"""

class InvalidAddressError(WalletError):
    """Raised for malformed crypto addresses"""

class NetworkTimeoutError(WalletError):
    """Raised on node connection failures"""

class TransactionSigningError(WalletError):
    """Raised when transaction validation fails"""

ERROR_MESSAGES = {
    InsufficientFundsError: "insufficient balance for transaction execution",
    InvalidAddressError: "invalid crypto address format provided",
    NetworkTimeoutError: "node connection timed out",
    TransactionSigningError: "failure during private key signature process"
}

def get_error_message(exception: Exception) -> str:
    return ERROR_MESSAGES.get(type(exception), "an unexpected error occurred")