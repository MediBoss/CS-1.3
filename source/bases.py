
#!python
import string
import sys

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
        - Parameters: 
            - digits: str -- string representation of number (in given base)
            - base: int -- base of given number
        - Returns: int -- integer representation of number (in base 10) """

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    length = len(digits)
    converted_digits = 0

    for digit in digits:
        length -= 1
        converted_digits += string.printable.index(digit.lower()) * pow(base, length)
    return converted_digits

def encode(number, base):
    """Encode given digits in given base to number in base 10.
        - Parameters: 
            - number: int -- integer representation of number (in base 10)
            - base: int -- base to convert to
        - Returns: str -- string representation of number (in given base) """

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)

    converted_value = ""
    if number == 0:
        return "0"

    while number != 0:
        remainder = string.printable[number % base]
        converted_value = str(remainder) + converted_value
        number = number // base
        
    return converted_value


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    - Parameters: 
        - digits: str -- string representation of number (in base1)
        - base1: int -- base of given number
        - base2: int -- base to convert to
    - Returns: str -- string representation of number (in base2)"""
    
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    base_ten = decode(digits, base1)
    result = str(encode(base_ten, base2))
    return result


def main():
    """Read command-line arguments and convert given digits between bases."""

    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
