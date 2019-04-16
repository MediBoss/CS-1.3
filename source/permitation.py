#!python


def permutation(string, left, right):
    """ Print all permutations of a string """
    return permutation_recursive(string, left, right)

def permutation_iterative(string):
    pass

def permutation_recursive(string, left, right):
    
    # Base case
    if left == right:
        print(str(string))

    # Recursive case
    for index in range(left, right + 1):
        string[left], string[index] = string[index], string[left]
        permutation_recursive(string, left+1, right)
        string[left], string[index] = string[index], string[left]

def main():

    word = "abc"
    print(permutation(list(word), 0, len(word)-1))

if __name__ == "__main__":
    main()

