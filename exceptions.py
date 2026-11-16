class WalletError(Exception):
    pass

class InsufficientFundsError(WalletError):
    pass

class ConnectionTimeoutError(WalletError):
    pass

class ValidationError(WalletError):
    pass

class TransactionExecutionError(WalletError):
    pass

def handle_crypto_exception(e: Exception) -> str:
    if isinstance(e, InsufficientFundsError):
        return "insufficient balance for transaction"
    if isinstance(e, ConnectionTimeoutError):
        return "network connection request timed out"
    if isinstance(e, ValidationError):
        return "invalid address or parameters provided"
    return "unhandled internal wallet error"