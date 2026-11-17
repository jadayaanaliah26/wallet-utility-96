import re

class WalletHandler:
    def __init__(self):
        self.address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')

    def is_valid_address(self, address: str) -> bool:
        return bool(self.address_pattern.match(address))

    def process_transactions(self, queue: list):
        processed = []
        for entry in queue:
            address = entry.get('address')
            amount = entry.get('amount')

            if not isinstance(address, str) or not self.is_valid_address(address):
                continue

            if not isinstance(amount, (int, float)) or amount <= 0:
                continue

            processed.append({
                'address': address,
                'amount': amount,
                'status': 'verified'
            })
        return processed

if __name__ == '__main__':
    handler = WalletHandler()
    mock_data = [
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 1.5},
        {'address': 'invalid_addr', 'amount': 0.5},
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': -1}
    ]
    results = handler.process_transactions(mock_data)
    print(results)