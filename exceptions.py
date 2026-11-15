class WalletError(Exception):
    def __init__(self, message: str, code: int = 500):
        super().__init__(message)
        self.message = message
        self.code = code


class InvalidAddressError(WalletError):
    def __init__(self, address: str, network: str = "mainnet"):
        super().__init__(f"Invalid {network} address format: '{address}'", code=400)
        self.address = address
        self.network = network


class InsufficientBalanceError(WalletError):
    def __init__(self, required: float, available: float, asset: str = "ETH"):
        super().__init__(
            f"Insufficient {asset} balance: required {required}, available {available}",
            code=402,
        )
        self.required = required
        self.available = available
        self.asset = asset


class NodeConnectionError(WalletError):
    def __init__(self, endpoint: str, details: str = ""):
        msg = f"Failed to connect to node at {endpoint}"
        if details:
            msg += f": {details}"
        super().__init__(msg, code=503)
        self.endpoint = endpoint


class KeyDerivationError(WalletError):
    def __init__(self, reason: str):
        super().__init__(f"Key derivation failed: {reason}", code=422)
        self.reason = reason
