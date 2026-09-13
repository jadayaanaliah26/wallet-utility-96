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
        self.logger.addHandler(handler)

    def log_error(self, operation: str, error: Exception) -> None:
        if not isinstance(error, Exception):
            self.logger.error(f'invalid error type in {operation}')
            return
        
        error_details = {
            'op': operation,
            'type': type(error).__name__,
            'msg': str(error)
        }
        self.logger.error(f'failed {operation}: {error_details}')

    def safe_execute(self, func: callable, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, ConnectionError) as e:
            self.log_error(func.__name__, e)
            return None
        except Exception as e:
            self.logger.critical(f'unexpected fatal error in {func.__name__}: {str(e)}')
            raise