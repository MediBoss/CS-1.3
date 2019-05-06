#!python

from binarytree import BinarySearchTree
from binarytree import BinaryTreeNode

class TreeMap(object):


    def __init__(self, init_size=8):
         """Initialize this TreeMap and insert the given items, if any."""
         self.buckets = [BinarySearchTree() for i in range(init_size)]
         self.size = 0

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def contains(self, key):
        
        bucket_index = self._bucket_index(key)
        target_bucket = self.buckets[bucket_index]

        

    def get(self, key):
        pass

    def set(self, key, value):
        
        bucket_index = self._bucket_index(key)
        target_bucket = self.buckets[bucket_index]
        is_found = target_bucket.contains(value)
        entry = (key,value)

        if is_found == False:
            target_bucket.insert(entry)
            self.size += 1

        else:
            # delete that entry
            pass

    def delete(self):
        pass
            

def main():
    
    treepMap = TreeMap()
    treepMap.set('Medi', 123)
    print(treepMap.contains('Medi'))

if __name__ == "__main__":
    main()