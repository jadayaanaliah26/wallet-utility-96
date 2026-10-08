class WalletError(Exception):
    """Base exception for wallet-utility-96"""

class ConfigurationError(WalletError):
    """Raised when config is invalid"""

class TransactionError(WalletError):
    """Raised during chain interaction failures"""

class ValidationError(WalletError):
    """Raised when data integrity is compromised"""

class InsufficientFundsError(TransactionError):
    """Raised when balance is too low"""

class NetworkTimeoutError(TransactionError):
    """Raised during RPC communication failures"""

class KeyManagementError(WalletError):
    """Raised during signing or key derivation"""