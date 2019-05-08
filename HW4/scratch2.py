class LinkedList:

    ### Nested class ###
    class _Node:
        __slots__ = '_element', '_next'

        # Node constructor
        def __init__(self, element, next):
            self._element = element
            self._next = next

    ####################

    # LinkedList constructor
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Insertion element x at the tail
    def insertTail(self, x):
        newNode = self._Node(x, None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode;
        self._size += 1

    # Remove the current head and return its element
    def removeHead(self):
        if self.isEmpty():
            raise Exception('List is empty')
        oldHead = self._head._element
        self._head = self._head._next
        self._size -= 1
        return oldHead

    # Check if list is empty
    def isEmpty(self):
        if self._size == 0:
            return True
        return False

    # Splices together 2 ordered LinkedLists and returns the result as a string
    def splice(self, l1, l2):
        if not self.isEmpty():  # Make sure list doesn't have any elements
            raise Exception('List already contains elements')
        s = ''
        e1 = l1.removeHead()    # Get head elements from each LinkedList
        e2 = l2.removeHead()
        while True:
            if e1 > e2:     # Insert in ascending order
                self.insertTail(e2)
                s = s + str(e2) + '->'
                while l2.isEmpty():     # insert remaining elements from l1
                    self.insertTail(e1)
                    s = s + str(e1) + '->'
                    if l1.isEmpty():  # return condition
                        return s[0:len(s) - 2]
                    e1 = l1.removeHead()
                e2 = l2.removeHead()
            else:
                self.insertTail(e1)
                s = s + str(e1) + '->'
                while l1.isEmpty():     # insert remaining elements from l2
                    self.insertTail(e2)
                    s = s + str(e2) + '->'
                    if l2.isEmpty():  # return condition
                        return s[0:len(s)-2]
                    e2 = l2.removeHead()
                e1 = l1.removeHead()

if __name__ == '__main__':
    # Construct list 1
    list1 = LinkedList()
    list1.insertTail(1)
    list1.insertTail(2)
    list1.insertTail(4)

    # Construct list 2
    list2 = LinkedList()
    list2.insertTail(1)
    list2.insertTail(3)
    list2.insertTail(4)

    # Construct list 3
    list3 = LinkedList()
    print(list3.splice(list1, list2))