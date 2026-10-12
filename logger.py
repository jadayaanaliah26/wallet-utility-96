import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Initialize and return a configured logger instance."""
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter: logging.Formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

def get_logger(name: str) -> logging.Logger:
    """Retrieve an existing logger or create a new one."""
    return logging.getLogger(name)

class WalletLogger:
    """Utility class for wallet-related logging operations."""
    def __init__(self, name: str) -> None:
        self.logger: logging.Logger = setup_logger(name)

    def info(self, message: str) -> None:
        """Log informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Log error messages with optional stack trace."""
        self.logger.error(message, exc_info=exc_info)