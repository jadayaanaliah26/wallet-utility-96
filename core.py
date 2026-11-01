import re
from decimal import Decimal, InvalidOperation
from typing import Dict, Any, Optional


class WalletError(Exception):
    pass


class InsufficientFundsError(WalletError):
    pass


class InvalidAddressError(WalletError):
    pass


class WalletCore:
    ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")

    def __init__(self, initial_balances: Optional[Dict[str, Decimal]] = None):
        self.balances: Dict[str, Decimal] = initial_balances or {}

    def validate_address(self, address: str) -> str:
        if not isinstance(address, str) or not self.ADDRESS_REGEX.match(address):
            raise InvalidAddressError(f"Invalid Ethereum address: {address}")
        return address.lower()

    def parse_amount(self, raw_amount: Any) -> Decimal:
        try:
            amount = Decimal(str(raw_amount))
        except (InvalidOperation, TypeError, ValueError) as err:
            raise WalletError(f"Cannot parse amount '{raw_amount}': {err}")

        if amount <= Decimal("0"):
            raise WalletError(f"Amount must be strictly positive: {amount}")

        return amount

    def transfer(self, sender: str, recipient: str, amount_raw: Any) -> Dict[str, Any]:
        sender_clean = self.validate_address(sender)
        recipient_clean = self.validate_address(recipient)
        amount = self.parse_amount(amount_raw)

        sender_balance = self.balances.get(sender_clean, Decimal("0"))
        if sender_balance < amount:
            raise InsufficientFundsError(
                f"Sender {sender_clean} has {sender_balance}, needs {amount}"
            )

        self.balances[sender_clean] = sender_balance - amount
        self.balances[recipient_clean] = self.balances.get(recipient_clean, Decimal("0")) + amount

        return {
            "status": "success",
            "sender": sender_clean,
            "recipient": recipient_clean,
            "amount": amount,
        }
