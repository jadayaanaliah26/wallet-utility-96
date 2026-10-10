import re

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')


def validate_address(address: str) -> bool:
    return bool(ADDRESS_PATTERN.match(address))


def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0


def process_transaction(address: str, amount: float) -> bool:
    if not validate_address(address):
        raise ValueError(f'invalid wallet address: {address}')
    if not validate_amount(amount):
        raise ValueError(f'invalid transaction amount: {amount}')
    return True


def transaction_loop(transactions: list) -> list:
    results = []
    for tx in transactions:
        try:
            if process_transaction(tx.get('addr'), tx.get('amount')):
                results.append({'status': 'success', 'data': tx})
        except ValueError as e:
            results.append({'status': 'error', 'message': str(e)})
    return results