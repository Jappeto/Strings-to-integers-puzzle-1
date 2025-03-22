#!/usr/bin/env python3

# ----------------------------------------------------------------------
# strToInt2.py
# Jacob Reppeto
# ----------------------------------------------------------------------

from typing import Dict, List, Optional


def strToInt2(s: str) -> Optional[int]:
    """
    Converts a string containing a mix of digits and written-out numbers
    into its integer representation.

    The function parses the input string `s` for both numeric characters
    and string representations of numbers (e.g., "one", "two") and combines
    them into a single integer. Non-numeric portions of the string are ignored.

    :param s: A string potentially containing digits and/or written-out numbers.
    :return: An integer representation of the extracted numbers, or None if
             no valid numeric data is found in the string.
    """
    numbers: dict[str, int] = { "zero": 0, "one": 1, "two": 2,
                                "three": 3, "four": 4, "five": 5,
                                "six": 6, "seven": 7, "eight": 8,
                                "nine": 9 }
    digits: list[int] = []

    for i in range(len(s)):
        # Check if the current character is a digit
        if s[i].isdigit():
            digits.append(int(s[i]))

        else:
            # Check if the current substring matches any of the number words
            for key, value in numbers.items():
                if s[i:].startswith(key):
                    digits.append(value)
                    break

    # If no digits were found, return None
    if len(digits) == 0:
        return None
    else:
        # Combine the digits into a single integer
        total = 0
        # Multiply the total by 10 and add the next digit
        for digit in digits:
            total = total * 10 + digit

        return total

def main():
    print(strToInt2("phonetw3oneighty"))  # Expected: 1318


# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()