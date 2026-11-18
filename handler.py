import re

class WalletHandler:
    def __init__(self):
        self.address_pattern = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

    def validate_input(self, address: str, amount: float) -> bool:
        if not self.address_pattern.match(address):
            return False
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        return True

    def process_queue(self, tasks: list):
        for task in tasks:
            address = task.get('address')
            amount = task.get('amount', 0)

            if not self.validate_input(address, amount):
                print(f'Invalid transaction data: {address}')
                continue

            self.execute_transfer(address, amount)

    def execute_transfer(self, address: str, amount: float):
        print(f'Transferring {amount} to {address}')

if __name__ == '__main__':
    handler = WalletHandler()
    data = [
        {'address': '0x1234567890abcdef1234567890abcdef12345678', 'amount': 1.5},
        {'address': 'invalid-address', 'amount': 0.1}
    ]
    handler.process_queue(data)