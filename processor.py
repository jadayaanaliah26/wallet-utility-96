from decimal import Decimal, InvalidOperation
from typing import Any, Dict


class ProcessingError(Exception):
    pass


class InvalidAddressError(ProcessingError):
    pass


class InsufficientBalanceError(ProcessingError):
    pass


class TransactionProcessor:
    def __init__(self, min_fee: Decimal = Decimal("0.0001")):
        self.min_fee = min_fee

    def validate_address(self, address: str) -> None:
        if not address or not isinstance(address, str):
            raise InvalidAddressError("Address must be a non-empty string")
        if not address.startswith("0x") or len(address) != 42:
            raise InvalidAddressError("Malformed blockchain address format")
        try:
            int(address[2:], 16)
        except ValueError:
            raise InvalidAddressError("Address contains invalid hex characters")

    def process_transaction(self, payload: Dict[str, Any]) -> Dict[str, str]:
        required_keys = {"sender", "recipient", "amount", "balance", "fee"}
        if not required_keys.issubset(payload.keys()):
            missing = required_keys - payload.keys()
            raise ProcessingError(f"Missing required fields: {missing}")

        self.validate_address(payload["sender"])
        self.validate_address(payload["recipient"])

        try:
            amount = Decimal(str(payload["amount"]))
            balance = Decimal(str(payload["balance"]))
            fee = Decimal(str(payload["fee"]))
        except (InvalidOperation, TypeError) as err:
            raise ProcessingError(f"Invalid numeric value in payload: {err}") from err

        if amount <= Decimal("0"):
            raise ProcessingError("Transaction amount must be positive")

        if fee < self.min_fee:
            raise ProcessingError(f"Fee below minimum threshold of {self.min_fee}")

        total_deduction = amount + fee
        if total_deduction > balance:
            raise InsufficientBalanceError("Insufficient funds for transfer")

        remaining = balance - total_deduction
        return {
            "status": "success",
            "sender": payload["sender"],
            "recipient": payload["recipient"],
            "amount": str(amount),
            "remaining_balance": str(remaining),
        }
