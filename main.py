SPACE = 1510
UNICODE_SCALAR_COUNT = 0x110000 - 0x800


def _shift_text(text: str, shift: int) -> str:
    result = []

    for c in text:
        codepoint = ord(c)
        if 0xD800 <= codepoint <= 0xDFFF:
            raise ValueError("Text must not contain Unicode surrogate characters.")

        scalar_index = codepoint if codepoint < 0xD800 else codepoint - 0x800
        shifted_index = (scalar_index + shift) % UNICODE_SCALAR_COUNT
        shifted_codepoint = (
            shifted_index if shifted_index < 0xD800 else shifted_index + 0x800
        )
        result.append(chr(shifted_codepoint))

    return ''.join(result)


def encode(text: str, key: int = 4, space: int = SPACE) -> str:
    return _shift_text(text, space + key)


def decode(e_text: str, key: int = 4, space: int = SPACE) -> str:
    return _shift_text(e_text, -(space + key))


if __name__ == '__main__':
    plain_text = input('Enter a text: ')
    key = 4

    e = encode(plain_text, key)
    print("Encoded:", e)

    p = decode(e, key)
    print("Decoded:", p)
