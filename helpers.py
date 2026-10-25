import re
from typing import Any, Dict, List


class WalletValidationError(Exception):
    pass


def validate_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def validate_transaction_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    required_keys = {"recipient", "amount", "nonce", "chain_id"}
    if not isinstance(payload, dict):
        raise WalletValidationError("Payload must be a dictionary")

    missing = required_keys - payload.keys()
    if missing:
        raise WalletValidationError(f"Missing fields: {', '.join(sorted(missing))}")

    recipient = payload["recipient"]
    if not validate_eth_address(recipient):
        raise WalletValidationError(f"Invalid Ethereum address: {recipient}")

    try:
        amount = float(payload["amount"])
        if amount <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        raise WalletValidationError("Amount must be a positive number")

    if not isinstance(payload["nonce"], int) or payload["nonce"] < 0:
        raise WalletValidationError("Nonce must be a non-negative integer")

    if not isinstance(payload["chain_id"], int) or payload["chain_id"] <= 0:
        raise WalletValidationError("Chain ID must be a positive integer")

    return {
        "recipient": recipient.lower(),
        "amount": amount,
        "nonce": payload["nonce"],
        "chain_id": payload["chain_id"],
    }


def process_batch_inputs(raw_inputs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    validated = []
    for idx, raw in enumerate(raw_inputs):
        try:
            item = validate_transaction_payload(raw)
            validated.append(item)
        except WalletValidationError as err:
            raise WalletValidationError(f"Invalid item at index {idx}: {err}")
    return validated
