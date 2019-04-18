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

        if self.is_empty():
            return None

        return self.list.head.data

    def length(self):

        return self.list.size

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        item = self.list.head.data
        
        if self.list.head == self.list.tail:
            self.tail = self.head = None
        else:
            self.list.head = self.list.head.next

        self.list.size -= 1
        return item

    def enqueue_front(self, item):
        self.list.prepend(item)

    def enqueue_back(self,item):
        self.list.append(item)

    def dequeue_front(self):
        pass

    def dequeue_back(self):
        pass


# Stack = LinkedStack
Deque = LinkedDeque
