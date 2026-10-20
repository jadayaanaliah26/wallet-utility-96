import logging
import sys
from typing import Optional

class WalletLogger:
    """Handles application logging for wallet-utility-96."""

    def __init__(self, name: str = "wallet-utility") -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational message."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log error message with optional exception trace."""
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(message)