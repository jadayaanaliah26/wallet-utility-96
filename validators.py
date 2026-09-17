import functools
from typing import Callable, Any

_CACHE_SIZE = 1024

def validate_address_format(address: str) -> bool:
    return len(address) == 42 and address.startswith('0x')

@functools.lru_cache(maxsize=_CACHE_SIZE)
def cached_address_validator(address: str) -> bool:
    return validate_address_format(address)

class AddressValidator:
    def __init__(self, validator_func: Callable[[str], bool] = cached_address_validator):
        self._validator = validator_func

    def validate(self, addresses: list[str]) -> list[bool]:
        return [self._validator(addr) for addr in addresses]

def batch_validate(addresses: list[str]) -> list[bool]:
    validator = AddressValidator()
    return validator.validate(addresses)

if __name__ == '__main__':
    sample = ['0x123' * 14, 'invalid', '0xabc' * 14]
    print(batch_validate(sample))