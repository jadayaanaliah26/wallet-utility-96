# wallet-utility-96

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`wallet-utility-96` is a lightweight Python toolkit designed for automated EVM wallet management, non-custodial balance tracking, and gas-optimized batch transactions. Built for crypto developers and bot operators, it simplifies multi-chain interactions across Ethereum, Polygon, and Arbitrum using direct Web3 RPC connections.

## Features

* **Multi-Chain Balance Auditing:** Query native and ERC-20 token balances simultaneously across custom RPC endpoints with built-in multicall support.
* **Batch Transaction Engine:** Send transfers to multiple destination addresses with automated nonce management and dynamic EIP-1559 gas pricing.
* **BIP-39 HD Wallet Derivation:** Generate and restore hierarchical deterministic wallets locally using standard 12 or 24-word seed phrases.
* **Keystore Encryption:** Encrypt and decrypt private keys on disk using AES-256-CBC for secure background task execution.

## Installation

Clone the repository and install the dependencies in a virtual environment:

```bash
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

The following example demonstrates loading an encrypted key and broadcasting a standard transaction:

```python
from wallet_utility import WalletManager

# Initialize the wallet manager with an RPC endpoint
wm = WalletManager(rpc_url="https://eth.llamarpc.com")

# Load encrypted wallet keystore
wallet = wm.load_keystore(path="keystore.json", password="securepassword123")

# Fetch current native balance
balance = wm.get_native_balance(wallet.address)
print(f"Address: {wallet.address} | Balance: {balance:.4f} ETH")

# Send a native asset transfer
tx_hash = wm.transfer_native(
    account=wallet,
    to_address="0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    amount=0.01
)
print(f"Transaction Hash: {tx_hash}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.