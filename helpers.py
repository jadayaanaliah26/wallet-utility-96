from decimal import Decimal, ROUND_DOWN
import hashlib
import re


def satoshi_to_btc(satoshi: int) -> Decimal:
    if satoshi < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return (Decimal(satoshi) / Decimal("100000000")).quantize(
        Decimal("0.00000001"), rounding=ROUND_DOWN
    )


def btc_to_satoshi(btc_amount: Decimal | float | str) -> int:
    val = Decimal(str(btc_amount))
    if val < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(val * Decimal("100000000"))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    if not address:
        return ""
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def double_sha256(data: bytes) -> str:
    first_hash = hashlib.sha256(data).digest()
    return hashlib.sha256(first_hash).hexdigest()


def is_hex_string(val: str) -> bool:
    if val.startswith(("0x", "0X")):
        val = val[2:]
    return bool(re.fullmatch(r"[0-9a-fA-F]+", val))
