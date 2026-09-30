import re

ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

class ValidationError(Exception):
    pass

def validate_transaction(data: dict) -> None:
    if not isinstance(data, dict):
        raise ValidationError('payload must be a dictionary')

    address = data.get('address')
    amount = data.get('amount')

    if not address or not ADDRESS_PATTERN.match(str(address)):
        raise ValidationError(f'invalid wallet address: {address}')

    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValidationError(f'invalid transaction amount: {amount}')

def process_loop(queue: list) -> None:
    for item in queue:
        try:
            validate_transaction(item)
            print(f'processing {item.get("address")}')
        except ValidationError as e:
            print(f'skip invalid item: {e}')

if __name__ == '__main__':
    mock_queue = [
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 0.5},
        {'address': 'invalid', 'amount': 1.2}
    ]
    process_loop(mock_queue)