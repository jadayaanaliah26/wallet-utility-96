import logging

class WalletError(Exception):
    pass

class InsufficientFundsError(WalletError):
    pass

class InvalidAddressError(WalletError):
    pass

def execute_transaction(wallet, amount: float, recipient: str):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError('Invalid transaction amount')

    if not recipient.startswith('0x') or len(recipient) != 42:
        raise InvalidAddressError(f'Invalid address format: {recipient}')

    try:
        if wallet.balance < amount:
            raise InsufficientFundsError(f'Balance {wallet.balance} insufficient for {amount}')
        
        wallet.balance -= amount
        return True
    except (InsufficientFundsError, InvalidAddressError) as e:
        logging.error(f'Transaction failed: {str(e)}')
        raise
    except Exception as e:
        logging.critical(f'Unexpected system error: {str(e)}')
        raise WalletError('System failure during execution')