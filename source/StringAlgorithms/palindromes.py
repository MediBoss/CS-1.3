#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


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
        Space Complexity : ??
    '''

    translator = str.maketrans('', '', string.punctuation)
    clean_string = text.translate(translator).replace(" ", "").lower()
    left = 0
    right = len(clean_string) - 1

    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
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
    # TODO : Fix this and pass last test cases
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).replace(" ", "").lower()

    # edge cases
    if len(text) == 0:
        return True

    if left == None:
        left = 0
        right = len(text) - 1 

    if left > right:
        return None

    # base case
    if text[left] != text[right]:
        return False
    
    # recursive case
    is_palindrome_recursive(text, left + 1, right - 1)
    return True

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