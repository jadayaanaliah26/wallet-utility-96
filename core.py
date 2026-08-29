from typing import Any, Dict, List
import hashlib

class Wallet:
    """A simple cryptocurrency wallet class."""

    def __init__(self, private_key: str) -> None:
        """Initialize the wallet with a private key."""
        self.private_key = private_key
        self.address = self._derive_address(private_key)
        self.balance: float = 0.0
        self.transactions: List[Dict[str, Any]] = []

    def _derive_address(self, private_key: str) -> str:
        """Derive address from private key using SHA256."""
        return hashlib.sha256(private_key.encode()).hexdigest()[:42]

    def get_balance(self) -> float:
        """Return the current wallet balance."""
        return self.balance

    def add_transaction(self, tx: Dict[str, Any]) -> None:
        """Add a transaction to the wallet history."""
        self.transactions.append(tx)
        if 'amount' in tx:
            self.balance += tx['amount']

    def send_funds(self, recipient: str, amount: float) -> bool:
        """Send funds to recipient if balance is sufficient."""
        if self.balance >= amount:
            self.balance -= amount
            tx = {'to': recipient, 'amount': -amount}
            self.add_transaction(tx)
            return True
        return False

    def get_transactions(self) -> List[Dict[str, Any]]:
        """Return list of all transactions."""
        return self.transactions


def create_wallet(seed: str) -> Wallet:
    """Create a new wallet from seed."""
    private_key = hashlib.sha256(seed.encode()).hexdigest()
    return Wallet(private_key)


def validate_wallet(wallet: Wallet) -> bool:
    """Validate if wallet has valid address."""
    return len(wallet.address) == 42


def process_batch(transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process a batch of transactions and return totals."""
    total_sent = 0.0
    for tx in transactions:
        if 'amount' in tx:
            total_sent += abs(tx['amount'])
    return {'total': total_sent, 'count': len(transactions)}