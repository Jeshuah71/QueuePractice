from Node import Node

class Queue:
    """Queue implementation using Nodes"""

    def __init__(self):
        """Create new queue"""
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """Returns a string representation of the queue, for example [a, b, c]"""
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return f"[{', '.join(map(str, items))}]"

    def enqueue(self, item):
        """Add an item to the queue"""
        new_node = Node(item)
        if self.tail: # Tail already exists
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1
    
    def dequeue(self):
        """Removes and returns an item from the queue"""
        #if there are no more items, a ValueError should be raised
        if self.is_empty():
            raise ValueError("Queue is empty")
        value = self.head.data
        self.head = self.head.next
        if self.head is None: 
            self.tail = None
        self.size -= 1 
        return value

    def is_empty(self):
        """Check if the queue is empty"""
        return self.size == 0

    def peek(self):
        """Get the value of the first item in the queue"""
        #if there are no more items None should be returned
        if self.is_empty():
            return None
        return self.head.data

    def size(self):
        """Get the number of items in the queue"""
        return self.size
