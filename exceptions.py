import re
from decimal import Decimal, InvalidOperation

class WalletError(Exception):
    pass

class InvalidAddressError(WalletError):
    pass

class InvalidAmountError(WalletError):
    pass

class InsufficientFundsError(WalletError):
    pass

def validate_address(address):
    if address is None:
        raise InvalidAddressError("Address cannot be None")
    if not isinstance(address, str):
        raise InvalidAddressError("Address must be a string")
    address = address.strip()
    if len(address) == 0:
        raise InvalidAddressError("Address cannot be empty")
    if len(address) < 26 or len(address) > 42:
        raise InvalidAddressError("Address length out of range")
    if address.startswith("0x"):
        if not re.match(r"^0x[a-fA-F0-9]{40}$", address):
            raise InvalidAddressError("Invalid Ethereum address format")
    else:
        if not re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", address):
            raise InvalidAddressError("Invalid Bitcoin address format")
    return address

def validate_amount(amount):
    if amount is None:
        raise InvalidAmountError("Amount cannot be None")
    try:
        dec_amount = Decimal(str(amount))
    except (InvalidOperation, TypeError, ValueError):
        raise InvalidAmountError("Amount must be a valid number")
    if dec_amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    return dec_amount

def validate_balance(balance):
    if balance is None:
        raise InvalidAmountError("Balance cannot be None")
    try:
        dec_balance = Decimal(str(balance))
    except (InvalidOperation, TypeError, ValueError):
        raise InvalidAmountError("Balance must be a valid number")
    if dec_balance < 0:
        raise InvalidAmountError("Balance cannot be negative")
    return dec_balance

def handle_transaction(address, amount, balance):
    try:
        address = validate_address(address)
        amount = validate_amount(amount)
        balance = validate_balance(balance)
        if amount > balance:
            raise InsufficientFundsError("Insufficient funds")
        return balance - amount
    except WalletError:
        raise
    except Exception as e:
        raise WalletError(str(e)) from e