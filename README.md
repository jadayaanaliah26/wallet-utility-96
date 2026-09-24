# wallet-utility-96

A high-performance Python toolkit designed for seamless cryptocurrency wallet management and cryptographic transaction signing. This utility streamlines address generation, balance verification, and secure key derivation for EVM-compatible chains.

## Features

*   **HD Wallet Derivation:** Support for BIP-39 mnemonic phrase generation and hierarchical deterministic key derivation.
*   **Balance Aggregation:** Efficiently fetch native token balances across multiple EVM networks using asynchronous RPC calls.
*   **Secure Transaction Signing:** Localized signing of raw transactions to ensure private keys never leave your execution environment.
*   **Gas Estimation:** Real-time fee calculation and optimization based on current network congestion data.

## Installation

Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

The following example demonstrates how to generate a new wallet and retrieve its address:

```python
from wallet_utility import WalletManager

# Initialize the manager
manager = WalletManager()

# Generate a new BIP-39 mnemonic and wallet
wallet = manager.create_wallet()

print(f"Mnemonic: {wallet.mnemonic}")
print(f"Address: {wallet.address}")
```

## Configuration

Set your RPC endpoints in the `.env` file to enable network-specific interactions:

```bash
RPC_ENDPOINT_MAINNET=https://eth-mainnet.alchemyapi.io/v2/your-api-key
RPC_ENDPOINT_POLYGON=https://polygon-rpc.com
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.