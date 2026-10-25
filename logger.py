import json
import logging
import sys
from datetime import datetime, timezone


class CryptoJsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        }
        if hasattr(record, "tx_hash"):
            log_payload["tx_hash"] = record.tx_hash
        if hasattr(record, "wallet_address"):
            log_payload["wallet_address"] = record.wallet_address
        if record.exc_info:
            log_payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_payload)


def setup_logger(name: str = "wallet_utility", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(CryptoJsonFormatter())
        logger.addHandler(handler)
    logger.propagate = False
    return logger


def log_transaction(logger: logging.Logger, level: int, msg: str, tx_hash: str, address: str) -> None:
    extra = {"tx_hash": tx_hash, "wallet_address": address}
    logger.log(level, msg, extra=extra)
