[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# wallet-utility-96

`wallet-utility-96` is a lightweight Python library designed to automate EVM wallet generation, balance tracking, and multi-chain transaction batching. It provides a unified asynchronous interface for interacting with Ethereum, Polygon, and Arbitrum RPC nodes securely.

## Features

* **Batch Balance Scanning:** Asynchronously fetch native asset and ERC-20 token balances across multiple chains simultaneously.
* **HD Wallet Derivation:** Generate BIP-39 seed phrases and derive standard BIP-44 keypairs for multi-account management.
* **EIP-1559 Fee Estimation:** Calculate real-time priority fees and max gas prices to prevent stuck transactions.
* **Encrypted Vault Storage:** Secure private key payloads locally using AES-256-GCM authenticated encryption.

## Installation

Install the package via standard Python tools:

```bash
pip install wallet-utility-96
```

Or install directly from the source repository:

```bash
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96
pip install .
```

## Basic Usage

```python
import asyncio
from wallet_utility_96 import WalletManager

async def main():
    # Initialize client for Ethereum mainnet
    manager = WalletManager(chain="ethereum", rpc_url="https://eth.llamarpc.com")

    # Generate a new BIP-39 wallet
    wallet = manager.create_wallet()
    print(f"New Address: {wallet.address}")

    # Fetch native ETH balance
    balance = await manager.get_balance(wallet.address)
    print(f"Balance: {balance.eth} ETH")

    # Encrypt keyphrase to disk
    manager.export_vault(wallet, password="SuperSecurePassword123", filepath="vault.json")

if __name__ == "__main__":
    asyncio.run(main())
```

## License

Distributed under the MIT License. See `LICENSE` for details.