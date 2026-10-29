from decimal import Decimal, ROUND_DOWN
import re

EVM_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def format_address(address: str, chars: int = 4) -> str:
    if not address or len(address) < (chars * 2 + 2):
        return address
    return f"{address[:chars + 2]}...{address[-chars:]}"


def to_base_unit(amount: str | float | Decimal, decimals: int = 18) -> int:
    val = Decimal(str(amount))
    factor = Decimal(10) ** decimals
    return int((val * factor).quantize(Decimal("1"), rounding=ROUND_DOWN))


def from_base_unit(amount: int, decimals: int = 18) -> Decimal:
    val = Decimal(amount)
    factor = Decimal(10) ** decimals
    return val / factor


def is_valid_evm_address(address: str) -> bool:
    return bool(EVM_ADDRESS_PATTERN.match(address))


def parse_transfer_log(raw_log: dict) -> dict:
    topics = raw_log.get("topics", [])
    data = raw_log.get("data", "0x")

    if len(topics) < 3:
        raise ValueError("Insufficient topics for ERC20 transfer event")

    from_address = "0x" + topics[1][-40:]
    to_address = "0x" + topics[2][-40:]

    clean_data = data[2:] if data.startswith("0x") else data
    raw_value = int(clean_data, 16) if clean_data else 0

    return {
        "from": from_address,
        "to": to_address,
        "value": raw_value,
    }
