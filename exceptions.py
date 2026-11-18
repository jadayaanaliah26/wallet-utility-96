class WalletError(Exception):
    def __init__(self, message: str, code: int = 1000, details: dict = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

    def to_dict(self) -> dict:
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
            "details": self.details,
        }


class InvalidAddressError(WalletError):
    def __init__(self, address: str, chain: str = "mainnet"):
        super().__init__(
            f"Invalid wallet address '{address}' for chain '{chain}'",
            code=1001,
            details={"address": address, "chain": chain},
        )


class InsufficientBalanceError(WalletError):
    def __init__(self, required: float, available: float, asset: str):
        super().__init__(
            f"Insufficient {asset}: required {required}, available {available}",
            code=1002,
            details={"required": required, "available": available, "asset": asset},
        )


class TransactionExecutionError(WalletError):
    def __init__(self, tx_hash: str, reason: str):
        super().__init__(
            f"Transaction {tx_hash} failed: {reason}",
            code=1003,
            details={"tx_hash": tx_hash, "reason": reason},
        )


class SignatureVerificationError(WalletError):
    def __init__(self, message: str = "Failed to verify signature"):
        super().__init__(message, code=1004)


def handle_rpc_error(response_data: dict) -> None:
    if "error" not in response_data:
        return
    err = response_data["error"]
    code = err.get("code", -1)
    msg = err.get("message", "Unknown RPC error")
    if code == -32602:
        raise InvalidAddressError(err.get("data", {}).get("address", "unknown"))
    raise WalletError(f"RPC node error ({code}): {msg}", code=code, details=err)