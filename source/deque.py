from linkedlist import LinkedList

class LinkedDeque(object):

    def __init__(self,iterable=None):

        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue_back(item)

    def is_empty(self):
        return self.list.size == 0

    def front(self):
        ''' Returns the element in the front of the queueu 
            Worst Case Runtime - O(1) since the front of the queue is the head of the linkedlist
        '''

        if self.is_empty():
            return None

        return self.list.head.data

    def length(self):

        return self.list.size


    def enqueue_front(self, item):
        ''' Adds an item in the front of the queue.
            Worst Case Runtime : O(1) O(1) since we're just preppending
        '''
        self.list.prepend(item)

    def enqueue_back(self,item):
        ''' Add an item in the back of the queue.
            Worst Case Runtime : O(1) since we're just appending
        '''
        self.list.append(item)

    def dequeue_front(self):
        ''' Pops and returns the element in the front of the queue.
            Worst Case Runtime : O(1) since we just re-arrange the head's pointer
        '''
        
        if self.is_empty():
            raise ValueError("Empty Queue")

        item = self.list.head.data
        
        if self.list.head == self.list.tail:
            self.tail = self.head = None
        else:
            self.list.head = self.list.head.next

        self.list.size -= 1
        return item

    def dequeue_back(self):
        ''' Pops and returns the element on the back of the queue.
            Worst Case Runtime : O(n) since we must re-arrange the tail's pointer
        '''
        
        if self.is_empty():
            raise ValueError("Empty queue")

        if self.list.tail:
            item = self.list.tail.data

        curr = self.list.head
        while curr is not None:
            if curr.next == self.list.tail:
                self.tail = curr
                self.tail.next = None
            curr = curr.next

        self.list.size -= 1
        return item
        

Deque = LinkedDeque
