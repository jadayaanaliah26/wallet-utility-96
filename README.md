[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# wallet-utility-96

`wallet-utility-96` is a lightweight Python toolkit designed to automate multi-chain EVM wallet generation, balance tracking, and transaction batching. Built for quantitative traders and web3 developers, it streamlines programmatic asset management across Ethereum, Polygon, and Arbitrum networks.

## Features

- **HD Wallet Derivation**: Generate hierarchical deterministic wallets using BIP-39 mnemonics and custom derivation paths.
- **Multi-Chain Balance Aggregation**: Asynchronously query ETH, MATIC, and arbitrary ERC-20 token balances in a single request.
- **Gas-Optimized Batching**: Package and broadcast multiple ERC-20 transfers concurrently to minimize gas overhead.
- **AES-256 Storage**: Encrypt keypairs locally using AES-256-GCM before persisting to disk.

## Installation

Install the package via `pip` from PyPI:

```bash
pip install wallet-utility-96
```

Or install directly from the source repository:

```bash
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96
pip install .
```

## Quickstart

The following example demonstrates how to create a new wallet, encrypt its credentials, and fetch current portfolio balances:

```python
from wallet_utility import KeyManager, WalletClient

# Initialize manager and generate a new HD wallet
km = KeyManager()
mnemonic, wallet = km.create_hd_wallet()

print(f"Address: {wallet.address}")
print(f"Mnemonic: {mnemonic}")

# Securely encrypt private key locally
encrypted_data = km.encrypt_private_key(wallet.private_key, password="StrongPassword123")

# Query multi-chain ERC-20 balances
client = WalletClient(provider_url="https://eth.llamarpc.com")
balances = client.get_token_balances(
    address=wallet.address,
    tokens=["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"]  # USDC Mainnet
)

print(balances)
```

## License

Distributed under the MIT License. See `LICENSE` for more information.