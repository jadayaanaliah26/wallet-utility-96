import logging
from typing import Callable, Any

logger = logging.getLogger("wallet_utility.handler")


class WalletError(Exception):
    pass


class InsufficientFundsError(WalletError):
    pass


class NetworkTimeoutError(WalletError):
    pass


class InvalidTransactionError(WalletError):
    pass


def execute_transaction_safely(
    func: Callable[..., Any], *args: Any, max_retries: int = 3, **kwargs: Any
) -> Any:
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except (ConnectionError, TimeoutError) as err:
            if attempt == max_retries - 1:
                raise NetworkTimeoutError(
                    "Node connection failed after maximum retries"
                ) from err
            logger.warning("Retrying connection following network error...")
        except ValueError as err:
            err_msg = str(err).lower()
            if "insufficient" in err_msg or "funds" in err_msg:
                raise InsufficientFundsError(
                    "Insufficient balance to cover gas or value"
                ) from err
            raise InvalidTransactionError(
                f"Malformed transaction parameter: {err}"
            ) from err
        except Exception as err:
            raise WalletError(f"Unexpected wallet execution failure: {err}") from err
