from typing import Dict, List, Optional
import os

class WalletConfig:
    """Configuration manager for crypto wallet utilities."""

    def __init__(self, network: str = "mainnet", api_key: Optional[str] = None) -> None:
        """Initialize the wallet configuration.
        Args:
            network: Blockchain network identifier.
            api_key: Authentication key for API access.
        """
        self.network: str = network
        self.api_key: Optional[str] = api_key or os.getenv("WALLET_API_KEY")
        self.endpoints: Dict[str, str] = {}
        self._initialize_endpoints()

    def _initialize_endpoints(self) -> None:
        """Populate endpoint mappings based on current network."""

        if self.network == "mainnet":
            self.endpoints = {
                "btc": "https://blockstream.info/api",
                "eth": "https://api.etherscan.io/api",
                "sol": "https://api.mainnet-beta.solana.com"
            }
        elif self.network == "testnet":
            self.endpoints = {
                "btc": "https://blockstream.info/testnet/api",
                "eth": "https://api-sepolia.etherscan.io/api",
                "sol": "https://api.testnet.solana.com"
            }
        else:
            self.endpoints = {}

    def get_endpoint(self, coin: str) -> Optional[str]:
        """Get the API endpoint for the specified coin.
        Args:
            coin: Cryptocurrency ticker symbol.
        Returns:
            Endpoint URL string or None.
        """
        return self.endpoints.get(coin.lower())

    def get_supported_coins(self) -> List[str]:
        """List all supported cryptocurrencies.
        Returns:
            List of coin symbols.
        """
        return list(self.endpoints.keys())

    def is_api_key_valid(self) -> bool:
        """Verify if a valid API key is configured.
        Returns:
            Boolean indicating key validity.
        """
        if self.api_key is None:
            return False
        return len(self.api_key) >= 16

def load_wallet_config(network: Optional[str] = None) -> WalletConfig:
    """Load and return a wallet configuration instance.
    Args:
        network: Optional network override.
    Returns:
        Configured WalletConfig object.
    """
    net = network or os.getenv("WALLET_NETWORK", "mainnet")
    key = os.getenv("WALLET_API_KEY")
    return WalletConfig(network=net, api_key=key)