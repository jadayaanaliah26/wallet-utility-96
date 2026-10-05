from typing import Optional

class WalletError(Exception):
    """Base exception class for wallet-utility-96."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when transaction amount exceeds balance."""
    def __init__(self, amount: float, balance: float) -> None:
        self.amount = amount
        self.balance = balance
        super().__init__(f"Required {amount} exceeds available {balance}")

class InvalidAddressError(WalletError):
    """Raised when the provided wallet address format is invalid."""
    def __init__(self, address: str, network: Optional[str] = None) -> None:
        self.address = address
        self.network = network
        message = f"Invalid address format '{address}' for network {network or 'default'}"
        super().__init__(message)

class ConnectionTimeoutError(WalletError):
    """Raised when node connectivity times out."""
    pass

class TransactionSigningError(WalletError):
    """Raised when cryptographic signature creation fails."""
    pass