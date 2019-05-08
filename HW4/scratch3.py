class LinkedQueue:

    ### Nested class ###

    class _Node:
        __slots__ = '_element', '_next'

        # Node constructor
        def __init__(self, element, next):
            self._element = element
            self._next = next

    ####################

    # LinkedQueue constructor
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Add object x at the rear of the queue
    def enqueue(self, x):
        newNode = self._Node(x, None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode;
        self._size += 1

    # Remove and return the first element of the queue
    def dequeue(self):
        if self.isEmpty():
            raise Exception('List is empty')
        oldHead = self._head._element
        self._head = self._head._next
        self._size -= 1
        return oldHead

    # Return the first element of the queue without removing it
    def first(self):
        return self._head._element;

    # Return the size of the queue
    def len(self):
        return self._size;

    # Check if list is empty
    def isEmpty(self):
        if self.len() == 0:
            return True
        return False

    # Returns whether object x is in the queue
    def search(self, x):
        if self.isEmpty():
            return False
        currNode = self._head
        while True:     # Loop through each node until a match is found
            if currNode._element == x:
                return True
            if currNode == self._tail:  # break condition
                break
            else:
                currNode = currNode._next
        return False


if __name__ == '__main__':
    myLinkedQueue = LinkedQueue()

    # Test search()
    print(myLinkedQueue.search(1))  # Return False
    print('-----')

    # Test enqueue()
    myLinkedQueue.enqueue(1)
    myLinkedQueue.enqueue(2)
    myLinkedQueue.enqueue(3)
    print(myLinkedQueue.search(1))  # Return True
    print(myLinkedQueue.search(2))  # Return True
    print(myLinkedQueue.search(3))  # Return True
    print('-----')

    # Test dequeue()
    print(myLinkedQueue.dequeue())  # Return 1
    print(myLinkedQueue.search(1))  # Return False
    print(myLinkedQueue.search(2))  # Return True
    print(myLinkedQueue.search(3))  # Return True
    print('-----')

    # Test len() and first()
    print(myLinkedQueue.len())  # Return 2
    print(myLinkedQueue.first())  # Return 2