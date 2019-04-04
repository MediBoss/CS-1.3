#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    
    # base case
    if index >= len(array):
        return None
    if array[index] == item:
        return index
    if len(array) == 0:
        return None

    # recursive case
    return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    '''
        Return the index of item in sorted array or None if item is not found
        Time Complexity: O(log n)(n= size of array) - Choice of the next element is one of several possibilities.
        Space Complexity: O(1)
    '''
    
    # Get the lowest and highest bound
    low_bound = 0
    high_bound = len(array) - 1

    while low_bound <= high_bound:

        middle = int((low_bound + high_bound)/2)
        if array[middle] == item:
            # return index if item found in middle
            return middle
        elif array[middle] > item:
            # Shift the higher bound to the left if element at middle index to too high
            high_bound = middle - 1
        elif array[middle] < item:
            # Shift the lower bound to the right if element at middle index to too high
            low_bound = middle + 1
    return None
    
def binary_search_recursive(array, item, left=None, right=None):
    
    # Edge case
    if left == None:
        left = 0
        right = len(array) - 1
        
    middle = int((left + right)/2)

    # Base cases
    if left > right:
        return None
    if array[middle] == item:
        return middle

    # Recursive cases
    if array[middle] > item:
        return binary_search_recursive(array, item, left, middle-1)
    if array[middle] < item:
        return binary_search_recursive(array, item, middle+1 , right)

    