class WalletError(Exception):
    """Base exception for all wallet operations."""
    pass


class InvalidAddressError(WalletError):
    """Raised when a cryptocurrency address is malformed or invalid."""

    def __init__(self, address: str, network: str = "mainnet"):
        self.address = address
        self.network = network
        super().__init__(f"Invalid {network} address: {address}")


class InsufficientFundsError(WalletError):
    """Raised when the wallet has insufficient balance for a transaction."""

    def __init__(self, required: float, available: float, asset: str):
        self.required = required
        self.available = available
        self.asset = asset
        super().__init__(
            f"Insufficient funds: required {required} {asset}, "
            f"but only have {available} {asset}"
        )


class TransactionSigningError(WalletError):
    """Raised when a transaction fails to be cryptographically signed."""

    def __init__(self, details: str):
        super().__init__(f"Transaction signing failed: {details}")


class NetworkProviderError(WalletError):
    """Raised when an external blockchain RPC or API provider fails."""

    def __init__(self, provider: str, status_code: int, message: str):
        self.provider = provider
        self.status_code = status_code
        super().__init__(
            f"Provider '{provider}' failed with status {status_code}: {message}"
        )
