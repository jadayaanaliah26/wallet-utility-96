class Base58Processor:
    ALPHABET = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    BASE = 58
    _DECODE_MAP = {char: index for index, char in enumerate(ALPHABET)}

    @classmethod
    def encode(cls, data: bytes) -> str:
        leading_zeros = len(data) - len(data.lstrip(b"\x00"))
        value = int.from_bytes(data, byteorder="big")
        result = bytearray()
        while value > 0:
            value, remainder = divmod(value, cls.BASE)
            result.append(cls.ALPHABET[remainder])
        result.extend([cls.ALPHABET[0]] * leading_zeros)
        return result[::-1].decode("ascii")

    @classmethod
    def decode(cls, data: str) -> bytes:
        raw_data = data.encode("ascii")
        leading_zeros = len(raw_data) - len(raw_data.lstrip(b"1"))
        value = 0
        for char in raw_data:
            value = value * cls.BASE + cls._DECODE_MAP[char]
        value_bytes = value.to_bytes((value.bit_length() + 7) // 8 or 1, byteorder="big")
        if value_bytes == b"\x00" and value == 0:
            value_bytes = b""
        return b"\x00" * leading_zeros + value_bytes