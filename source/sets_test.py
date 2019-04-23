from sets import Sets
import unittest

class SetsTest(unittest.TestCase):
    
    def test_init_with_no_element(self):
        set = Sets()
        assert set.size == 0


    def test_add(self):
        set = Sets()
        assert set.size == 0
        set.add('A')
        set.add('B')
        assert set.size == 2

    def test_size(self):
        set = Sets()
        assert set.size == 0
        set.add('A')
        set.add('B')
        set.add('C')
        set.add('D')
        set.add('F')
        assert set.size == 5

    def test_contains(self):
        set = Sets()
        set.add('A')
        set.add('B')

        # Assert True
        assert set.contains('A') == True
        assert set.contains('B') == True

        # Assert False
        assert set.contains('E') == False
        assert set.contains('F') == False

    def test_remove(self):
        
        # Adding elements
        set = Sets()
        set.add('A')
        set.add('B')

        # Deleting elements
        set.remove('A')
        assert set.size == 1
        set.remove('B')
        assert set.size == 0

        with self.assertRaises(KeyError):
            set.remove('B')


    def test_union(self):
        set_A = Sets()
        set_B = Sets()

        set_A.add('Medi')
        set_A.add('Mace')
        set_B.add('Yves')
        set_B.add('Sarin')

        assert type(set_A.union(set_B) ) == list # should return a list
        assert set_A.size == 2 # set A should retain its original size
        assert set_B.size == 2 # set B should retain its original size

        union_result = set_A.union(set_B)
        assert len(union_result) ==  4 # the result of the union should have a size of set A+B

    def test_intersection(self):
        set_A = Sets()
        set_B = Sets()

        set_A.add('Ronaldo')
        set_A.add('Mbappe')
        set_A.add('Neymar')
        set_A.add('Messi')

        set_B.add('Rashford')
        set_B.add('Mbappe')
        set_B.add('Neymar')
        set_B.add('DeBruyne')

        assert type(set_A.intersection(set_B) ) == list # should return a list
        assert len(set_A.intersection(set_B)) == 2 # Only two element are interscted
        assert set_A.size == 4 # set A should retain its original size
        assert set_B.size == 4 # set B should retain its original size

        # Testing elements in return list to be True
        intersection_result = set_A.intersection(set_B)
        assert 'Neymar' in intersection_result
        assert 'Mbappe' in intersection_result

        # Testing elements not in return list to be True
        assert 'Rashford' not in intersection_result 
        assert 'Ronaldo' not in intersection_result
        assert 'Deybrune' not in intersection_result 
        assert 'Messi' not in intersection_result


    def test_difference(self):
        set_A = Sets()
        set_B = Sets()

        set_A.add('Ronaldo')
        set_A.add('Mbappe')
        set_A.add('Neymar')
        set_A.add('Messi')

        set_B.add('Rashford')
        set_B.add('Mbappe')
        set_B.add('Neymar')
        set_B.add('DeBruyne')


        difference_result = set_A.difference(set_B)
        assert type(difference_result) == list # should return a list
        assert set_A.size == 4 # set A should retain its original size
        assert set_B.size == 4 # set B should retain its original size
        
        # Testing for Element in SET A not in SET B 
        assert 'Ronaldo' in difference_result
        assert 'Messi' in difference_result

        # Testing intersecting elements are not in the difference
        assert 'Neymar' not in difference_result
        assert 'Mbappe' not in difference_result

        # Testing for Element in SET B not in SET A
        difference_result = set_B.difference(set_A)
        assert 'DeBruyne' in difference_result
        assert 'Rashford' in difference_result

    def test_is_subset(self):
        set_A = Sets()
        set_B = Sets()

        set_A.add('Ronaldo')
        set_A.add('Mbappe')
        set_A.add('Neymar')
        set_A.add('Messi')

        set_B.add('Mbappe')
        set_B.add('Neymar')

        is_subset_result = set_A.is_subset(set_B)
        assert type(is_subset_result) == bool # should return a list
        assert set_A.size == 4 # set A should retain its original size
        assert set_B.size == 2 # set B should retain its original size
        assert set_B.is_subset(set_A) == True # SET B's elements are all in SET A

        set_B.add('Pele') # Added an element in SET B that is not in set A
        assert set_B.is_subset(set_A) == False #  SET B's elements are not all in SET A


    if __name__ == '__main__':
        unittest.main()