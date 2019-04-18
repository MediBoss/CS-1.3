#!python

from deque import Deque
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        dq = Deque()
        assert dq.front() is None
        assert dq.length() == 0
        assert dq.is_empty() is True

    def test_init_with_list(self):
        dq = Deque(['A', 'B', 'C'])
        assert dq.front() == 'A'
        assert dq.length() == 3
        assert dq.is_empty() is False

    def test_enqueue_front(self):
        dq = Deque()
        assert dq.length() == 0
        assert dq.front() is None

        dq.enqueue_front('Medi')
        assert dq.front() == 'Medi'
        assert dq.length() == 1

        dq.enqueue_front('Yves')
        assert dq.front() == 'Yves'
        assert dq.length() == 2

    def test_enqueue_back(self):
        dq = Deque()
        assert dq.length() == 0
        assert dq.front() is None

        dq.enqueue_back('Medi')
        assert dq.front() == 'Medi'
        assert dq.length() == 1

        dq.enqueue_back('Yves')
        assert dq.front() == 'Medi' # front should still be Medi
        assert dq.length() == 2 


    def test_dequeue_front(self):

        dq = Deque(['Medi', 'Yves', 'AL'])
        assert dq.length() == 3
        assert dq.front() == 'Medi'

        dq.dequeue_front()
        assert dq.length() == 2

        dq.dequeue_front()
        assert dq.length() == 1

        dq.dequeue_front()
        assert dq.length() == 0
        assert dq.front() is None


    def test_dequeue_back(self):

        dq = Deque(['Medi', 'Yves', 'AL'])
        assert dq.length() == 3
        assert dq.front() == 'Medi'

        dq.dequeue_back() == 'AL'
        assert dq.length() == 2

        dq.dequeue_back() == 'Yves'
        assert dq.length() == 1

        dq.dequeue_back() == 'Medi'
        assert dq.length() == 0

if __name__ == '__main__':
    unittest.main()