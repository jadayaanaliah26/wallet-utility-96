class WalletError(Exception):
    """Base exception for wallet-utility-96"""

class InsufficientFundsError(WalletError):
    """Raised when wallet balance is too low"""

class InvalidAddressError(WalletError):
    """Raised when the address format is incorrect"""

class ConnectionTimeoutError(WalletError):
    """Raised when node communication fails"""

class TransactionRejectedError(WalletError):
    """Raised when the network rejects a broadcast"""

class SignatureError(WalletError):
    """Raised when cryptographic signing fails"""

class ValidationError(WalletError):
    """Raised for input validation failures"""