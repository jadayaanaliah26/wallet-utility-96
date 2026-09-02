import re
from decimal import Decimal
def is_valid_address(address):
    if not isinstance(address, str):
        return False
    if len(address) < 26 or len(address) > 35:
        return False
    pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
    return bool(re.match(pattern, address))
def is_valid_amount(amount_str):
    try:
        amount = Decimal(amount_str)
        return amount > 0
    except Exception:
        return False
def process_operation(address, amount):
    print('Processed:', amount, 'BTC to', address)
    return True
def main():
    transactions = [
        {'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': '50'},
        {'address': '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2', 'amount': '1.5'},
        {'address': 'invalidaddr', 'amount': '10'},
        {'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': '0'},
        {'address': '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy', 'amount': '2.0'}
    ]
    for tx in transactions:
        addr = tx['address']
        amt = tx['amount']
        if not is_valid_address(addr):
            print('Invalid address skipped:', addr)
            continue
        if not is_valid_amount(amt):
            print('Invalid amount skipped:', amt)
            continue
        process_operation(addr, amt)
    print('All transactions processed')
if __name__ == '__main__':
    main()