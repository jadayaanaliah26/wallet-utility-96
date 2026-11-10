class WalletError(Exception):
    """Base exception for wallet-utility-96"""


class InsufficientFundsError(WalletError):
    """Raised when transaction exceeds balance"""


class NetworkConnectionError(WalletError):
    """Raised when node connectivity fails"""


class InvalidAddressError(WalletError):
    """Raised when address format is invalid"""


class SigningError(WalletError):
    """Raised when transaction signing fails"""


class ConfigurationError(WalletError):
    """Raised when environment setup is incomplete"""


class RateLimitError(WalletError):
    """Raised when API thresholds are exceeded"""


class DecryptionError(WalletError):
    """Raised when key retrieval fails"""