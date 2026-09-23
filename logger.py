import logging
import sys
from typing import Any

class WalletLogger:
    def __init__(self, name: str = "wallet-utility-96") -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, message: str, context: Any = None) -> None:
        if context:
            self.logger.error(f"{message} | context: {context}")
        else:
            self.logger.error(message)

    def safe_execution(self, func, *args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            self.log_error("invalid input value", str(ve))
        except ConnectionError as ce:
            self.log_error("network connectivity issue", str(ce))
        except Exception as e:
            self.log_error("unexpected system failure", str(e))
        return None

logger = WalletLogger()