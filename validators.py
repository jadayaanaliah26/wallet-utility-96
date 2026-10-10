import re

class AddressValidator:
    ETH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
    BTC_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$')

    @staticmethod
    def is_valid_eth(address: str) -> bool:
        return bool(AddressValidator.ETH_PATTERN.match(address))

    @staticmethod
    def is_valid_btc(address: str) -> bool:
        return bool(AddressValidator.BTC_PATTERN.match(address))

class AmountValidator:
    @staticmethod
    def is_positive_decimal(amount: str) -> bool:
        try:
            value = float(amount)
            return value > 0
        except ValueError:
            return False

    @staticmethod
    def is_within_limit(amount: float, max_limit: float) -> bool:
        return 0 < amount <= max_limit

def validate_transaction_data(data: dict) -> bool:
    required_fields = ['address', 'amount', 'currency']
    if not all(field in data for field in required_fields):
        return False

    if data['currency'] == 'ETH':
        return AddressValidator.is_valid_eth(data['address'])
    if data['currency'] == 'BTC':
        return AddressValidator.is_valid_btc(data['address'])
    
    return False