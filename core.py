import hashlib
import re
from typing import Dict, Optional, Union


class WalletManager:
    """Manages cryptocurrency wallet operations including validation and key generation."""

    ETH_ADDRESS_PATTERN = r"^0x[a-fA-F0-9]{40}$"

    def __init__(self, network: str = "mainnet") -> None:
        """Initialize the wallet manager with a specific network."""
        self.network = network
        self._balances: Dict[str, float] = {}

    def is_valid_eth_address(self, address: str) -> bool:
        """Validate an Ethereum wallet address format using regex pattern."""
        if not isinstance(address, str):
            return False
        return bool(re.match(self.ETH_ADDRESS_PATTERN, address))

    def generate_address_checksum(self, address: str) -> Optional[str]:
        """Generate a deterministic mock checksum for an address."""
        if not self.is_valid_eth_address(address):
            return None
        clean_addr = address.lower().replace("0x", "")
        hashed = hashlib.sha256(clean_addr.encode()).hexdigest()
        return f"0x{hashed[:40]}"

    def update_balance(self, address: str, amount: Union[int, float]) -> bool:
        """Update the tracked balance for a given wallet address."""
        if not self.is_valid_eth_address(address) or amount < 0:
            return False
        self._balances[address] = float(amount)
        return True

    def get_balance(self, address: str) -> float:
        """Retrieve the balance of a tracked address, defaulting to zero."""
        return self._balances.get(address, 0.0)
