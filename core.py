import logging
from typing import Optional, Dict, Any

class WalletError(Exception):
    pass

class WalletProcessor:
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def process_transaction(self, amount: float) -> Dict[str, Any]:
        try:
            if amount <= 0:
                raise ValueError("Transaction amount must be positive")
            
            if amount > self.balance:
                raise WalletError("Insufficient funds for transaction")

            self.balance -= amount
            return {"status": "success", "remaining": self.balance}

        except ValueError as e:
            logging.error(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}
        except WalletError as e:
            logging.error(f"Execution error: {e}")
            return {"status": "error", "message": str(e)}
        except Exception as e:
            logging.critical(f"Unexpected system failure: {e}")
            return {"status": "error", "message": "Internal system failure"}

    def update_balance(self, new_balance: float) -> bool:
        if not isinstance(new_balance, (int, float)) or new_balance < 0:
            return False
        self.balance = float(new_balance)
        return True