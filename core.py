import re

class WalletProcessor:
    def __init__(self):
        self.address_regex = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')

    def is_valid_amount(self, amount: str) -> bool:
        try:
            val = float(amount)
            return val > 0
        except (ValueError, TypeError):
            return False

    def is_valid_address(self, address: str) -> bool:
        return bool(self.address_regex.match(address))

    def run_loop(self, queue: list):
        for item in queue:
            address = item.get('address')
            amount = str(item.get('amount', '0'))

            if not self.is_valid_address(address):
                print(f'Invalid address: {address}')
                continue

            if not self.is_valid_amount(amount):
                print(f'Invalid amount: {amount}')
                continue

            self.process_transaction(address, float(amount))

    def process_transaction(self, address: str, amount: float):
        print(f'Processing {amount} to {address}')

if __name__ == '__main__':
    processor = WalletProcessor()
    test_queue = [
        {'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': '0.5'},
        {'address': 'invalid_addr', 'amount': '0.1'},
        {'address': '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy', 'amount': '-5'}
    ]
    processor.run_loop(test_queue)