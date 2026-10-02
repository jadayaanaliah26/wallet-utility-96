from typing import Dict, Any, Optional

class WalletHandler:
    """Handles crypto wallet balance and transaction validation."""

    def __init__(self, currency: str) -> None:
        self.currency: str = currency
        self.cache: Dict[str, float] = {}

    def get_balance(self, address: str) -> float:
        """Retrieve balance for a specific wallet address."""
        return self.cache.get(address, 0.0)

    def update_balance(self, address: str, amount: float) -> None:
        """Update local balance cache for the given address."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.cache[address] = amount

    def validate_address(self, address: str) -> bool:
        """Verify address format matches currency requirements."""
        if self.currency == "BTC":
            return address.startswith("1") or address.startswith("3")
        if self.currency == "ETH":
            return address.startswith("0x") and len(address) == 42
        return False

    def process_transaction(self, sender: str, receiver: str, amount: float) -> Optional[Dict[str, Any]]:
        """Execute validated transaction between wallets."""
        if not self.validate_address(sender) or not self.validate_address(receiver):
            return None
        
        sender_balance = self.get_balance(sender)
        if sender_balance < amount:
            return None
            
        self.update_balance(sender, sender_balance - amount)
        self.update_balance(receiver, self.get_balance(receiver) + amount)
        return {"status": "success", "amount": amount}