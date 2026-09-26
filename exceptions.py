class WalletError(Exception):
    """Base exception for wallet-utility-96"""

class InsufficientFundsError(WalletError):
    """Raised when transaction exceeds balance"""

class ConnectionTimeoutError(WalletError):
    """Raised when network requests time out"""

class ValidationError(WalletError):
    """Raised when input parameters are invalid"""

class KeyManagementError(WalletError):
    """Raised during encryption or signing failures"""

class ProtocolError(WalletError):
    """Raised when node communication fails"""

class RateLimitError(WalletError):
    """Raised when API request limits exceeded"""

class TransactionError(WalletError):
    """Raised when blockchain broadcast fails"""