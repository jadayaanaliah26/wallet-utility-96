import decimal
import re
from typing import Dict, Any, List


class ValidationError(Exception):
    pass


class TransactionProcessor:
    ADDRESS_REGEX = re.compile(r"^(0x[a-fA-F0-9]{40}|[13][a-km-zA-HJ-NP-Z1-9]{26,33})$")

    def __init__(self) -> None:
        self.processed_transactions: List[Dict[str, Any]] = []

    def validate_transaction(self, tx_data: Dict[str, Any]) -> Dict[str, Any]:
        address = tx_data.get("address")
        amount_str = tx_data.get("amount")

        if not address or not isinstance(address, str):
            raise ValidationError("Invalid or missing recipient address")

        if not self.ADDRESS_REGEX.match(address):
            raise ValidationError("Address format is invalid")

        if not amount_str:
            raise ValidationError("Missing transaction amount")

        try:
            amount = decimal.Decimal(str(amount_str))
        except (ValueError, decimal.InvalidOperation):
            raise ValidationError("Amount must be a valid numeric value")

        if amount <= decimal.Decimal("0"):
            raise ValidationError("Amount must be greater than zero")

        return {"address": address, "amount": amount}

    def process_batch(self, transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        success_count = 0
        failures = []

        for index, tx in enumerate(transactions):
            try:
                validated_tx = self.validate_transaction(tx)
                self.processed_transactions.append(validated_tx)
                success_count += 1
            except ValidationError as err:
                failures.append({"index": index, "error": str(err)})

        return {
            "success_count": success_count,
            "failures": failures
        }