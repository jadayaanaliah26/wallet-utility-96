import logging
import re
from typing import Union

class CryptoSanitizingFormatter(logging.Formatter):
    """Formatter that redacts potential private keys from logs."""

    PRIVATE_KEY_REGEX = re.compile(r"\b[a-fA-F0-9]{64}\b")

    def format(self, record: logging.LogRecord) -> str:
        original_msg = super().format(record)
        return self.PRIVATE_KEY_REGEX.sub("[REDACTED_KEY]", original_msg)

def get_logger(name: str, level: Union[int, str] = logging.INFO) -> logging.Logger:
    """Configure and return a sanitized console logger for the wallet utility."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = CryptoSanitizingFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger