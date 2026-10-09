"""Custom exception classes for wallet operations."""

from typing import Optional


class WalletError(Exception):
    """Base exception for all wallet utility errors."""

    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.code: Optional[int] = code


class InvalidAddressError(WalletError):
    """Raised when a cryptocurrency address format is invalid."""

    def __init__(self, address: str, network: str = "mainnet") -> None:
        self.address: str = address
        self.network: str = network
        super().__init__(f"Invalid {network} address: {address}")


class InsufficientBalanceError(WalletError):
    """Raised when an account balance is insufficient for a transaction."""

    def __init__(self, required: float, available: float, currency: str = "ETH") -> None:
        self.required: float = required
        self.available: float = available
        self.currency: str = currency
        msg = f"Insufficient {currency}: required {required}, available {available}"
        super().__init__(msg, code=402)


class TransactionSigningError(WalletError):
    """Raised when signing a transaction payload fails."""

    def __init__(self, tx_hash: str, reason: str) -> None:
        self.tx_hash: str = tx_hash
        self.reason: str = reason
        super().__init__(f"Failed to sign transaction {tx_hash}: {reason}")


class NetworkAPIError(WalletError):
    """Raised when a crypto RPC or API request fails."""

    def __init__(self, endpoint: str, status_code: int) -> None:
        self.endpoint: str = endpoint
        self.status_code: int = status_code
        super().__init__(
            f"API call to {endpoint} failed with status {status_code}",
            code=status_code,
        )
