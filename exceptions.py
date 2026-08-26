class WalletError(Exception):
    """Base exception for all wallet utility errors."""
    pass


class InsufficientFundsError(WalletError):
    """Raised when a wallet lacks sufficient balance for a transaction."""
    def __init__(self, required: float, available: float) -> None:
        self.required: float = required
        self.available: float = available
        message: str = f"Insufficient funds: required {required}, available {available}"
        super().__init__(message)


class InvalidAddressError(WalletError):
    """Raised when a provided cryptocurrency address is malformed."""
    def __init__(self, address: str, currency: str) -> None:
        self.address: str = address
        self.currency: str = currency
        message: str = f"Invalid {currency} address format: {address}"
        super().__init__(message)


class TransactionError(WalletError):
    """Raised when a transaction fails to sign or broadcast."""
    def __init__(self, txid: str, reason: str) -> None:
        self.txid: str = txid
        self.reason: str = reason
        message: str = f"Transaction {txid} failed: {reason}"
        super().__init__(message)
