class WalletError(Exception):
    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class InvalidAddressError(WalletError):
    def __init__(self, address: str, chain: str = "mainnet"):
        message = f"Invalid {chain} address format: {address}"
        super().__init__(message, {"address": address, "chain": chain})


class InsufficientFundsError(WalletError):
    def __init__(self, required: float, available: float, asset: str = "ETH"):
        message = f"Insufficient {asset}: required {required}, available {available}"
        super().__init__(
            message,
            {"required": required, "available": available, "asset": asset},
        )


class NonceConflictError(WalletError):
    def __init__(self, expected: int, received: int):
        message = f"Nonce mismatch: expected {expected}, got {received}"
        super().__init__(message, {"expected": expected, "received": received})


class TransactionSimulationError(WalletError):
    def __init__(self, reason: str, raw_tx: str | None = None):
        message = f"Simulation failed: {reason}"
        super().__init__(message, {"reason": reason, "raw_tx": raw_tx})


class RPCProviderError(WalletError):
    def __init__(self, endpoint: str, status_code: int | None = None):
        message = f"RPC node failure at {endpoint} (status: {status_code})"
        super().__init__(
            message, {"endpoint": endpoint, "status_code": status_code}
        )
