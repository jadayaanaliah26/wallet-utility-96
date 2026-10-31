class WalletError(Exception):
    """Base exception for wallet-utility-96 operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when wallet balance is below transaction requirement."""
    def __init__(self, required: float, available: float) -> None:
        super().__init__(f"Required {required}, but only {available} available.")
        self.required = required
        self.available = available

class ConnectionTimeoutError(WalletError):
    """Raised when blockchain node fails to respond."""
    def __init__(self, endpoint: str, timeout: int) -> None:
        super().__init__(f"Connection to {endpoint} timed out after {timeout}s.")
        self.endpoint = endpoint

class InvalidAddressError(WalletError):
    """Raised when provided crypto address format is invalid."""
    def __init__(self, address: str) -> None:
        super().__init__(f"Invalid address format: {address}")
        self.address = address

class TransactionSigningError(WalletError):
    """Raised during failure to sign cryptographic transactions."""
    def __init__(self, message: str) -> None:
        super().__init__(f"Signing failed: {message}")