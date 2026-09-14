[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# wallet-utility-96

`wallet-utility-96` is a lightweight Python toolkit designed for secure Ethereum-compatible wallet generation, multi-chain balance tracking, and offline transaction signing. It provides developers with a streamlined, low-dependency interface to interact with EVM-based chains without the overhead of massive web3 frameworks.

## Features

* **HD Wallet Derivation:** Generate secure 12 or 24-word BIP-39 mnemonics and derive private keys using standard BIP-44 pathways.
* **Multi-Chain Auditing:** Fetch native gas and ERC-20 token balances across Ethereum, Arbitrum, Optimism, and Polygon.
* **Air-Gapped Signing:** Sign raw transactions offline to ensure private keys never expose themselves to online network interfaces.

## Installation

Install the package and its cryptographic dependencies via pip:

```bash
pip install wallet-utility-96 eth-keys bip-utils requests
```

## Quick Start

Generate a new wallet and check its balance using a public RPC node:

```python
from wallet_utility_96 import WalletManager, ChainAuditor

# Create a secure HD wallet
wallet = WalletManager.generate_hd_wallet(words=12)
print(f"Mnemonic: {wallet.mnemonic}")
print(f"Address: {wallet.address}")

# Audit wallet balance on Ethereum Mainnet
auditor = ChainAuditor(rpc_url="https://cloudflare-eth.com")
balance_eth = auditor.get_balance(wallet.address)
print(f"Balance: {balance_eth} ETH")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.