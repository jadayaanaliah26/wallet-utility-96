import logging
import sys
from typing import Optional

class WalletLogger:
    def __init__(self, name: str = "wallet-utility-96", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        if not self.logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = False) -> None:
        self.logger.error(msg, exc_info=exc_info)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

def get_logger(name: str = "wallet-utility-96") -> logging.Logger:
    return WalletLogger(name).logger