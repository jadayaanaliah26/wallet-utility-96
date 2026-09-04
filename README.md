# wallet-utility-96

A high-performance Python toolkit designed for secure mnemonic generation, HD wallet derivation, and multi-chain address validation. This utility streamlines cryptographic workflows by providing a unified interface for interacting with BIP-39 seed phrases and extended private keys.

## Features

*   **BIP-39 Compliance**: Generate cryptographically secure 12, 18, or 24-word mnemonics with built-in checksum validation.
*   **Hierarchical Deterministic (HD) Derivation**: Derive master keys and child addresses using standard derivation paths (BIP-44/49/84).
*   **Multi-Chain Support**: Compatible with EVM-based networks and UTXO-based chains via extensible provider classes.
*   **Zero-Dependency Core**: Lightweight architecture focused on security and auditability by minimizing external runtime requirements.

## Installation

Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone https://github.com/Developer/wallet-utility-96.git
cd wallet-utility-96

# Install requirements
pip install -r requirements.txt
```

## Basic Usage

The following snippet demonstrates how to generate a new BIP-39 mnemonic and derive a private key for the default derivation path:

```python
from wallet_utility import WalletManager

# Initialize the manager
manager = WalletManager()

# Generate a new secure seed
mnemonic = manager.generate_mnemonic(strength=128)
print(f"Mnemonic: {mnemonic}")

# Derive private key from seed
private_key = manager.derive_private_key(mnemonic, path="m/44'/60'/0'/0/0")
print(f"Derived Key: {private_key}")
```

## Security Notice
This utility is intended for developer research and integration testing. Never hardcode mnemonics or private keys in source control; always utilize environment variables or hardware security modules (HSM) for production key management.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.