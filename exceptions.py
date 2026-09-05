class WalletError(Exception):
    """Base exception for wallet-utility-96"""


class ConnectionError(WalletError):
    """Raised on network communication failures"""


class TransactionError(WalletError):
    """Raised on invalid blockchain transactions"""


class ValidationError(WalletError):
    """Raised on input validation failure"""


class InsufficientFundsError(TransactionError):
    """Raised when wallet balance is too low"""


class InvalidKeyError(WalletError):
    """Raised when cryptographic keys are malformed"""


class RateLimitError(WalletError):
    """Raised when API request limits are exceeded"""
