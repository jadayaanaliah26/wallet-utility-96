import logging
import sys
from typing import Any

class WalletLogger:
    def __init__(self, name: str = 'wallet-utility-96'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, message: str, exc: Exception) -> None:
        error_type = type(exc).__name__
        self.logger.error(f'{message} | type: {error_type} | detail: {str(exc)}')

    def safe_execution(self, func: Any, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            self.log_error('network connectivity failure', e)
        except ValueError as e:
            self.log_error('invalid input data processing', e)
        except Exception as e:
            self.log_error('unexpected runtime critical failure', e)
        return None

logger = WalletLogger()