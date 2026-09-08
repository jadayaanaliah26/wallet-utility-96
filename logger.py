import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path('logs')
LOG_FILE = LOG_DIR / 'wallet.log'

def setup_logger(name: str = 'wallet_utility') -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    file_handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logger()