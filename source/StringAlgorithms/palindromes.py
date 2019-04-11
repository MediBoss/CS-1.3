#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

LETTERS = frozenset(string.ascii_letters)
def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    ''' Returns a boolean statement on wheter a string is spelled identicall backward
        Params : 
            - text : the string input
        Return:
            - Bool : a true or false value
        Time Complexity: O(n) where n the length of the string
        Space Complexity : O(n) where n is the number of char in the string
    '''

    # cleans up the text input
    translator = str.maketrans('', '', string.punctuation) # O(p) time and space where p is the # of punc
    clean_string = text.translate(translator).replace(" ", "") #  2n = O(n) 

    # grab the left and right bound to keep track 
    left = 0
    right = len(clean_string) - 1

    while left < right: #(n/2) iteration = O(n)
        if clean_string[left].lower() != clean_string[right].lower(): # O(1)
            # Return false if the element at the left and right aren't equivalent
            return False

        # Adjust the bounds for the next iteration
        left += 1
        right -= 1

    return True

def is_palindrome_alternative(text):
    ''' Alternative solution by comparing the reverse of the string 
        Time Complexity : O(n) where n is the lenght of the string
        Space Complexity : O(n) since we are copying a new string and slicing
    '''
    translator = str.maketrans('', '', string.punctuation)
    clean_string = text.translate(translator).replace(" ", "").lower()
    return clean_string == clean_string[::-1]

def is_palindrome_recursive(text, left=None, right=None):
    ''' Recursive solution to palindrome problem with bounds.
        Time Complexity : O(n log n) because we are calling the function n/2 and replace, lower are O(n)
        Space Complexity : O(n) since we are re-copying a cleaner text input
    '''
    # edge cases
    if left == None:
        left = 0
        right = len(text) - 1 

    if left >= right:
        return True

    # Skips oiver unwanted characters(e.g : ?,!,.)
    if text[left] not in LETTERS:
        return is_palindrome_recursive(text, left + 1, right)
    if text[right] not in LETTERS:
        return is_palindrome_recursive(text, left, right -1 )

    if text[left] != text[right]:
    # checks if the issue is with capitalization
        if text[left].lower() != text[right].lower():
            return False
 
    return is_palindrome_recursive(text, left + 1, right - 1)


def main():

    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()