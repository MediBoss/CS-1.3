from doublylinkedlist import DoublyLinkedList, Node
import unittest

class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        # Initializer should add instance properties
        assert node.data is data
        assert node.next is None

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None


    # Function to test finding a data from the doubly linked list
    def test_find(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.find(lambda item: item == 'B') == 'B'  # Match equality
        assert dll.find(lambda item: item < 'B') == 'A'  # Match less than
        assert dll.find(lambda item: item > 'B') == 'C'  # Match greater than
        assert dll.find(lambda item: item == 'X') is None  # No matching item

    # Function to test appending data in the doubly linked list
    def test_append(self):
        dll = DoublyLinkedList()
        dll.append('M')
        assert dll.head.data == 'M'
        assert dll.tail.data == 'M'
        dll.append('E')
        assert dll.head.data == 'M'
        assert dll.tail.data == 'E'

    # Function to test prepending data in the doubly linked list
    def test_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend('M')
        assert dll.head.data == 'M'
        assert dll.tail.data == 'M'
        dll.prepend('E')
        assert dll.head.data == 'E'
        assert dll.tail.data == 'M'

    # Function to test the length of dll with a counter
    def test_length_counter(self):
        dll = DoublyLinkedList()
        assert dll.length_with_counter() == 0
        dll.append('L')
        dll.append('K')
        assert dll.length_with_counter() == 2

    # Function to test the length of dll by traversing
    def test_length(self):
        dll = DoublyLinkedList()
        assert dll.length() == 0
        dll.append('L')
        dll.append('K')
        assert dll.length() == 2

    def test_delete(self):
        dll = DoublyLinkedList()
        dll.append('L')
        dll.append('K')
        dll.append('G')

        dll.delete('L')
        assert dll.head.data == 'K'
        assert dll.tail.data =='G'
        assert dll.length() == 2
        print(dll)

        dll.delete('K')
        assert dll.head.data == 'G'
        assert dll.tail.data == 'G'
        assert dll.length() == 1

        dll.delete('G')
        assert dll.head == None
        assert dll.tail == None
        assert dll.length() == 0



if __name__ == '__main__':
        unittest.main()