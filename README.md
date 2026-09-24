# wallet-utility-96

`wallet-utility-96` is a lightweight, command-line interface tool designed to streamline hierarchical deterministic (HD) wallet operations. It provides a secure environment for managing private keys, signing transactions, and batch-processing cryptocurrency addresses.

## Features

*   **BIP-39 Mnemonic Generation:** Securely generate and derive HD wallet keys using standard entropy sources.
*   **Multi-Chain Support:** Native compatibility with EVM-based networks and Bitcoin-style address derivation.
*   **Secure Offline Signing:** Sign raw transactions locally to ensure sensitive private keys never touch the network.
*   **CSV Batch Processing:** Effortlessly generate or validate hundreds of addresses from a single master seed in seconds.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96
pip install -r requirements.txt
```

## Usage

Generate a new wallet and derive the first five addresses on the Ethereum derivation path:

```bash
python main.py generate --path "m/44'/60'/0'/0" --count 5
```

To sign a transaction using a stored mnemonic file:

```bash
python main.py sign --input tx_data.json --key-file .secret_mnemonic
```

*Note: Always handle your mnemonic phrases with caution. Never share your seed or store it in plain text on unencrypted devices.*

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.