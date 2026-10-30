import logging
import sys
from typing import Optional

class WalletLogger:
    def __init__(self, name: str = "wallet-utility-96", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_wallet_logger(name: str = "wallet-utility-96") -> logging.Logger:
    return WalletLogger(name).get_logger()

logger = get_wallet_logger()