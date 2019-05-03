#!python
from treemap import TreeMap
import unittest 


class TreeMapTest(unittest.TestCase):

    def test_init(self):
        
        treepMap = TreeMap()

        assert treepMap.size == 0