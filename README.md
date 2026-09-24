[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# wallet-utility-96

`wallet-utility-96` is a lightweight Python toolkit designed for automated EVM wallet management, transaction batching, and balance tracking across multiple blockchain networks. It streamlines decentralized interactions by providing secure key derivation, gas optimization, and real-time token allowance audits.

## Features

- **Multi-Chain Balance Auditing:** Fetch native and ERC-20 token balances concurrently across Ethereum, Arbitrum, Polygon, and Binance Smart Chain using Web3 RPC nodes.
- **Batch Token Transfers:** Execute optimized EIP-1559 transactions to distribute native assets or ERC-20 tokens to multiple recipient addresses in a single run.
- **BIP-39 HD Key Derivation:** Generate and manage hierarchical deterministic wallets securely from standard seed phrases using custom derivation paths.
- **Allowance Security Scanning:** Identify and revoke stale token approvals across decentralized exchanges to mitigate smart contract exposure.

## Installation

Clone the repository and install the dependencies in a virtual environment:

```bash
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96
python3 -m venv venv
source venv/bin/activate
pip install web3 eth-account bip_utils
```

## Quick Start

Initialize the `WalletManager` with an RPC endpoint to audit balances and check contract permissions:

```python
from wallet_utility import WalletManager

# Initialize for Ethereum Mainnet
rpc_url = "https://rpc.ankr.com/eth"
wm = WalletManager(rpc_node=rpc_url)

# Audit a public wallet address
target_address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

# Fetch native ETH balance
balance = wm.get_eth_balance(target_address)
print(f"Address: {target_address}")
print(f"ETH Balance: {balance:.4f} ETH")

# Scan active ERC-20 allowances
active_approvals = wm.get_active_allowances(target_address)
print(f"Found {len(active_approvals