class WalletError(Exception):
    """Base exception for all wallet operations."""
    pass


class InvalidAddressError(WalletError):
    """Raised when a cryptocurrency address format is invalid."""

    def __init__(self, address: str, chain: str = "unknown"):
        self.address = address
        self.chain = chain
        super().__init__(f"Invalid {chain} address format: '{address}'")


class InvalidPrivateKeyError(WalletError):
    """Raised when a private key fails validation."""

    def __init__(self, message: str = "Invalid private key provided"):
        super().__init__(message)


class InsufficientFundsError(WalletError):
    """Raised when a wallet has insufficient balance for a transaction."""

    def __init__(self, required: float, available: float, asset: str):
        self.required = required
        self.available = available
        self.asset = asset
        super().__init__(
            f"Insufficient funds for {asset}: required {required}, available {available}"
        )


class TransactionError(WalletError):
    """Raised when a transaction broadcast or signing fails."""

    def __init__(self, tx_hash: str, message: str):
        self.tx_hash = tx_hash
        super().__init__(f"Transaction {tx_hash} failed: {message}")


class NodeConnectionError(WalletError):
    """Raised when connection to RPC node fails."""

    def __init__(self, endpoint: str, message: str = "Connection failed"):
        self.endpoint = endpoint
        super().__init__(f"Node error at {endpoint}: {message}")
