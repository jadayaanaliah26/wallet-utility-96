import logging
import sys
from typing import Optional

class WalletLogger:
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.handler.setFormatter(self.formatter)
        if not self.logger.handlers:
            self.logger.addHandler(self.handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc: Optional[Exception] = None) -> None:
        if exc:
            self.logger.error(f"{msg}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

def get_logger(name: str) -> WalletLogger:
    return WalletLogger(name)