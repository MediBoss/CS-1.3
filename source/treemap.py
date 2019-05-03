#!python

from binarytree import BinarySearchTree
from binarytree import BinaryTreeNode

class TreeMap(object):


    def __init__(self, init_size=8):
         """Initialize this TreeMap and insert the given items, if any."""
         self.buckets = [BinarySearchTree() for i in range(init_size)]
         self.size = 0

    