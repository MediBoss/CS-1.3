'''
Given two array of words, return an array that contains words in first array that aren't in the second array.
'''

def redact_words(words, banned_words):

    set_two = set(banned_words) #O(n)
    return_sets = []
    for word in words:
        if word not in set_two:
            return_sets.append(word)

    return return_sets
