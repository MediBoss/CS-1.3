class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# The doubly linked list class
class DoublyLinkedList(object):

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.counter = 0

        # if Initialized with items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this doubly linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'DoublyLinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""

        items = []
        current_node = self.head
        while current_node is not None:
            self.counter += 1
            items.append(current_node.data)
            current_node = current_node.next

        return items

    # function that retruns a boolean value if the list is empty or not
    def is_empty(self):
        return self.head is None

    def length(self):
        counter = 0
        curr_node = self.head

        while curr_node is not None:
            counter += 1
            curr_node = curr_node.next

        return counter

    def length_with_counter(self):
        return self.counter

    # This functions retruns a boolean on wheter or not the data is found in the list
    def find(self, quality):

        current_node = self.head
        while current_node is not None:
            if quality(current_node.data) is True:
                return current_node.data
            current_node = current_node.next

    # This function replaces a data from the list with a new one
    def replace(self, old_item, new_item):
        """Replace the given old item from this doubly linked list with the new item.
        TODO: Best case running time: O(???) Why and under what conditions?"""

        current_node = self.head
        while current_node is not None:
            if current_node.data == old_item:
                current_node.data = new_item
                return
            current_node = current_node.next

        raise ValueError("Old item was not found")

    def append(self, data):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.counter += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.counter += 1

    def prepend(self, data):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""

        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.counter += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.counter += 1

    def delete(self, data):
        """Delete the given item from this doubly linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
            # checks if the list is empty
        if self.is_empty():
            raise ValueError("Empty List")
        # check if item is in head
        if self.head.data == data:
            self.head = self.head.next
            #checks if the head and tail point to same object(ll with one item)
            if self.tail.data == data:
                self.tail = None
            self.counter -= 1
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                current_node.prev.next = current_node.next
                self.counter -= 1
                #checks if deleted node was the tail
                if self.tail.data == data:
                    #updates the tail
                    self.tail = current_node
                return
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(data))