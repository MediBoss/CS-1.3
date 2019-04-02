
#!python
import string
import sys

BASE_36 = {"A": 10, "B": 11,"C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17,"I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,"U": 30, "V": 31, "W": 32, "X": 33, "Y":34, "Z": 35}
BINARY_TO_HEXA = {1: "", 2:"", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "","A": 10, "B": 11,"C": 12, "D": 13, "E": 14, "F": 15}
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
        if digit in BASE_36:
            digit = BASE_36.get(digit)

        converted_digits += (int(digit) * pow(base, length))
    return converted_digits
    

def encode(number, base):
    """Encode given digits in given base to number in base 10.
        - Parameters: 
            - number: int -- integer representation of number (in base 10)
            - base: int -- base to convert to
        - Returns: str -- string representation of number (in given base) """

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)

    mutated_number = number
    converted_value = ""
    if base == 2:
        while mutated_number > 0:
            result, remainder = (mutated_number/base, mutated_number%base)
            converted_value += str(remainder)
            mutated_number = result

    elif base == 16 or base == 36:
        quotient, remainder = (number/base, number%base)
        while quotient > 0:
            if find_key(remainder) is not None:
                converted_value += find_key(remainder)
            else:
                converted_value += str(remainder)
            
            quotient, remainder = (quotient/base, quotient%base)
    return converted_value[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    - Parameters: 
        - digits: str -- string representation of number (in base1)
        - base1: int -- base of given number
        - base2: int -- base to convert to
    - Returns: str -- string representation of number (in base2)"""
    
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # conversion 2 <-> 10
    if base1 == 2 and base2 == 10:
        return decode(digits, base1)
    # conversion 10 <-> 2
    elif base1 == 10 and base2 == 2:
        return encode(int(digits), base2)

    # conversion 2 <-> 16
    # TODO: Convert digits from base 2 to base 16 (and vice versa)

    # conversion 10 <-> 16
    elif base1 == 10 and base2 == 16:
        return encode(int(digits), base2)
    # conversion 16 <-> 10
    elif base1 == 16 and base2 == 10:
        return decode(digits, base1)

    # conversion any base <-> any base
    # TODO: Convert digits from any base to any base (2 up to 36)


def find_key(target_value):
    ''' Find the key of a given value in a dictionary '''
    for key,value in BASE_36.items():
        if value == target_value:
            return key
    return None

def main():
    """Read command-line arguments and convert given digits between bases."""

    number = "7E"
    print(convert(number, 16, 10))
    # import sys
    # args = sys.argv[1:]  # Ignore script file name
    # if len(args) == 3:
    #     digits = args[0]
    #     base1 = int(args[1])
    #     base2 = int(args[2])
    #     # Convert given digits between bases
    #     result = convert(digits, base1, base2)
    #     print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    # else:
    #     print('Usage: {} digits base1 base2'.format(sys.argv[0]))
    #     print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
