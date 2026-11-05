import logging
import sys
from typing import Optional

class WalletLogger:
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_wallet_logger(name: str = "wallet-utility-96") -> logging.Logger:
    return WalletLogger(name).get_logger()