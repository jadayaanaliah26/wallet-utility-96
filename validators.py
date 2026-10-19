import re

class WalletValidator:
    ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

    @staticmethod
    def validate_address(address: str) -> bool:
        return bool(WalletValidator.ADDRESS_PATTERN.match(address))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

def process_transaction(data: dict):
    addr = data.get("address")
    amt = data.get("amount")

    if not WalletValidator.validate_address(addr):
        raise ValueError(f"invalid wallet address: {addr}")
    
    if not WalletValidator.validate_amount(amt):
        raise ValueError(f"invalid transaction amount: {amt}")

    return True

def run_main_loop(queue):
    for entry in queue:
        try:
            if process_transaction(entry):
                print(f"processed: {entry.get('address')}")
        except (ValueError, TypeError) as e:
            print(f"validation failure: {e}")