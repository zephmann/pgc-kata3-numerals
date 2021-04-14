# :coding: utf-8


NUMERAL_CHARACTERS = [
    "I",  # one
    "V",  # five
    "X",  # ten
    "L",  # fifty
    "C",  # hundred
    "D",  # five hundred
    "M",  # thousand
]


def convert(value: int) -> str:
    """Convert an integer *value* into a string of Roman numerals."""
    # TODO validate input

    digits = map(int, reversed(list(str(value))))
    
    numerals = ""
    for exp, digit in enumerate(digits):
        # skip any zeros
        if not digit:
            continue

        numerals = _convert_digit(digit, exp) + numerals

    return numerals


def _convert_digit(digit: int, exp: int) -> str:
    """Helper function to convert a single digit."""
    char_offset = exp * 2
    ones = NUMERAL_CHARACTERS[char_offset]

    try:
        fives = NUMERAL_CHARACTERS[char_offset + 1]
        tens = NUMERAL_CHARACTERS[char_offset + 2]
    except IndexError:
        fives = ""
        tens = ""

    if digit == 9:
        return f"{ones}{tens}"

    if digit == 4:
        return f"{ones}{fives}"

    numerals = f"{fives}" if digit > 4 else ""

    numerals += f"{ones}" * (digit % 5)

    return numerals
