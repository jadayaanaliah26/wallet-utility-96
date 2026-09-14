import hashlib
import secrets

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    n = int.from_bytes(data, "big")
    result = []
    while n > 0:
        n, r = divmod(n, 58)
        result.append(BASE58_ALPHABET[r])
    zeros = 0
    for byte in data:
        if byte == 0:
            zeros += 1
        else:
            break
    return (BASE58_ALPHABET[0] * zeros) + "".join(reversed(result))


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def generate_private_key() -> str:
    return secrets.token_hex(32)


def wei_to_ether(wei: int) -> float:
    return wei / (10**18)


def ether_to_wei(ether: float) -> int:
    return int(ether * (10**18))
