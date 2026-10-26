class WalletError(Exception):
    """Base exception for wallet-utility-96"""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is insufficient"""
    pass

class InvalidAddressError(WalletError):
    """Raised when address checksum fails"""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when RPC connection times out"""
    pass

class TransactionRejectedError(WalletError):
    """Raised when network rejects signature"""
    pass

class DecryptionError(WalletError):
    """Raised when key store unlock fails"""
    pass