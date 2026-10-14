import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "wallet.log"


def setup_logger(name: str) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=5
    )
    handler.setFormatter(formatter)
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.addHandler(console)
    
    return logger