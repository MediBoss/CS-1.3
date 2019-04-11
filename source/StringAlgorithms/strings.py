#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
        Time Complexity : O(n/m) where n is the the size of text and m is the size of pattern
        Space Complexity : O(n) since we are slicing a new string at each iteration
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Edge case - the text contains empty pattern or pattern equivalent to it
    if pattern == '' or text == pattern:
        return True

    # Set the bounds needed for slicing and getting each substring
    initial_count = 0
    count = len(pattern)

    # Keeps track of the range when slicing the string
    while count <= len(text):
        # Grabs a substring with the same length as the pattern
        curr_value = text[initial_count:count]
        if curr_value == pattern:
            # True is returned if the substring is equal to the pattern
            return True

        # Increment the bounds for next iterations
        initial_count += 1
        count += 1

    return False # False is returned if line 21 is never executed to True

    



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    
    # edge case
    if len(pattern) == 0:
        return 0

    count = 1
    splitted_arr = []
    while count <= len(text):
        if text[0:count] == pattern:
            splitted_arr=  text.split(text[count])
        count += 1

    for index, elem in enumerate(splitted_arr):
        if elem == pattern:
            return index

    # better solution



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


# def test_string_algorithms(text, pattern):
#     found = contains(text, pattern)
#     print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
#     # TODO: Uncomment these lines after you implement find_index
#     #index = find_index(text, pattern)
#     print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
#     # TODO: Uncomment these lines after you implement find_all_indexes
#     #indexes = find_all_indexes(text, pattern)
#     print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    print(contains("abc", "ab"))
    # import sys
    # args = sys.argv[1:]  # Ignore script file name
    # if len(args) == 2:
    #     text = args[0]
    #     pattern = args[1]
    #     test_string_algorithms(text, pattern)
    # else:
    #     script = sys.argv[0]
    #     print('Usage: {} text pattern'.format(script))
    #     print('Searches for occurrences of pattern in text')
    #     print("\nExample: {} 'abra cadabra' 'abra'".format(script))
    #     print("contains('abra cadabra', 'abra') => True")
    #     print("find_index('abra cadabra', 'abra') => 0")
    #     print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()