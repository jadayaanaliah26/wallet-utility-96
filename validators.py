import re

class WalletValidator:
    ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

    @staticmethod
    def validate_address(address: str) -> bool:
        return bool(WalletValidator.ADDRESS_PATTERN.match(address))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

def process_transaction(data: dict) -> bool:
    address = data.get('address', '')
    amount = data.get('amount', 0)

    if not WalletValidator.validate_address(address):
        return False

    if not WalletValidator.validate_amount(amount):
        return False

    return True

def run_processing_loop(queue: list):
    for entry in queue:
        try:
            if process_transaction(entry):
                print(f"Processing {entry.get('address')}")
            else:
                print(f"Invalid transaction data: {entry}")
        except Exception:
            continue