#!python

from hashtable import HashTable
class Sets(object):
    
    def __init__(self, iterator=None):
        """Initialize this set and push the given items, if any."""

        self.size = 0
        self.hashTable = HashTable()

        # Adds element in the hash table if the set is initialized with elements
        if iterator is not None:
            for element in iterator:
                self.hashTable.set(element, element)

    def contains(self, element):
        ''' Return True or False on if element is in the set
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''
        # check if the element is already in the set to avoid duplicates
        if self.contains(element):
            return
        return self.hashTable.contains(element)
    
    def add(self, element):
        ''' Pushes an element into the set
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''

        self.hashTable.set(element, element)
        self.size += 1

    def remove(self, element):
        ''' Removes an element from the set
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''

        self.hashTable.delete(element)
        self.size -= 1


    def union(self, other_set):
        ''' Return elements from both sets combined
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''
        return self.hashTable.keys() + other_set.hashTable.keys()

    def intersection(self, other_set):

        ''' Return ONLY elements that are seen in both sets
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''
        
        array_one = self.hashTable.keys()
        array_two = other_set.hashTable.keys()
        intersection_list = list()

        for element in array_one:
            if element in array_two:
                intersection_list.append(element)

        return intersection_list

    def difference(self, other_set):
        ''' Return elements from self(which is a set) that are not seen in other_set
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''
        
        difference_result = list()
        intersecting_elements = self.intersection(other_set)
        first_set_keys = self.hashTable.keys()

        for element in first_set_keys:
            if element not in intersecting_elements:
                difference_result.append(element)

        return difference_result

    def is_subset(self, other_set):
        ''' Return True or False if all element from self(which is a set) are seen in other_set
            Time Complexity(WC) : 
            Space Complexity(WC) : 
        '''
        
        for element in self.hashTable.keys():
            if element not in other_set.hashTable.keys():
                return False
        return True