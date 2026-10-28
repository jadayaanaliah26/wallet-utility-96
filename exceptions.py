class WalletError(Exception):
    """Base exception for wallet-utility-96."""
    pass

class ValidationError(WalletError):
    """Raised when input fails validation."""
    pass

class AddressFormatError(ValidationError):
    """Raised for malformed crypto addresses."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when balance is too low."""
    pass

def validate_address(address: str, chain: str) -> None:
    if not address or len(address) < 26:
        raise AddressFormatError(f"Invalid {chain} address format")

def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValidationError("Amount must be positive")

def process_input(data: dict) -> None:
    try:
        validate_address(data.get("to"), data.get("chain"))
        validate_amount(data.get("amount", 0))
    except (AddressFormatError, ValidationError) as e:
        raise ValidationError(f"Input validation failed: {str(e)}") from e