import logging
import sys
from typing import Optional

class WalletLogger:
    """Standardized logging utility for wallet-utility-96."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg: str, *args: object) -> None:
        """Log info level message."""
        self.logger.info(msg, *args)

    def error(self, msg: str, exc_info: bool = True) -> None:
        """Log error level message with traceback."""
        self.logger.error(msg, exc_info=exc_info)

def get_logger(name: str, level: Optional[int] = None) -> WalletLogger:
    """Factory function to instantiate a wallet logger."""
    log_level = level or logging.INFO
    return WalletLogger(name, log_level)