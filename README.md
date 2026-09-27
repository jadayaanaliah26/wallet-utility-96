# wallet-utility-96

`wallet-utility-96` is a high-performance Python toolkit designed for secure management and batch processing of cryptocurrency wallets. It provides developers with a streamlined interface for key generation, address derivation, and automated balance reconciliation across multiple EVM-compatible chains.

### Key Features

*   **BIP-39 Implementation:** Secure generation of 12/24-word recovery phrases with entropy validation.
*   **Multi-Chain Support:** Native derivation paths for Ethereum, Polygon, BSC, and Arbitrum.
*   **Balance Aggregation:** Optimized asynchronous fetching of token balances to bypass rate-limiting during batch lookups.
*   **Keystore Encryption:** AES-256-GCM encryption for local private key storage and handling.

### Installation

Requires Python 3.9 or higher. Clone the repository and install dependencies via pip:

```bash
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96
pip install -r requirements.txt
```

### Usage

This snippet demonstrates how to generate a new wallet and derive the primary address:

```python
from wallet_utility import WalletManager

# Initialize manager
manager = WalletManager()

# Generate new mnemonic and derive keys
wallet = manager.create_new_wallet()
print(f"Address: {wallet.address}")
print(f"Private Key: {wallet.private_key}")

# Check balance on Ethereum Mainnet
balance = manager.get_balance(wallet.address, chain='eth')
print(f"Current Balance: {balance} ETH")
```

### Security Disclaimer
This utility is intended for developer environments. Always ensure private keys are stored in encrypted environments and never commit sensitive keys to version control systems.

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.