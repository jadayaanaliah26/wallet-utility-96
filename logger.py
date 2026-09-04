import logging
import sys
from typing import Any

class WalletLogger:
    def __init__(self, name: str = 'wallet-utility-96'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def log_error(self, message: str, context: dict[str, Any] | None = None) -> None:
        payload = f"error: {message}"
        if context:
            payload += f" | context: {context}"
        self.logger.error(payload)

    def handle_exception(self, exc: Exception, context: dict[str, Any] | None = None) -> None:
        error_details = {
            'type': type(exc).__name__,
            'args': str(exc.args),
        }
        if context:
            error_details.update(context)
        self.log_error(str(exc), error_details)

def get_logger() -> WalletLogger:
    return WalletLogger()