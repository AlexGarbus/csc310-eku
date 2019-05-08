class MyCircularDeque:
    # constructor
    def __init__(self, k):
        self._data = [None] * k
        self._maxSize = k;
        self._size = 0;
        self._front = 0
        self._back = k-1

    # insertion methods
    def insertFront(self, x):
        if self._size == self._maxSize:  # queue is full
            return False
        self._data.insert(0, x)
        self._size += 1
        return True
    def insertLast(self, x):
        if self._size == self._maxSize:  # queue is full
            return False
        self._data[self._size] = x
        self._size += 1
        return True

    # deletion methods
    def deleteFront(self):
        if self._size == 0:  # queue is empty
            return False
        self._data.pop(0)
        self._data.append(None)
        self._size -= 1
        return True
    def deleteLast(self):
        if self._size == 0:  # queue is empty
            return False
        self._data[self._size - 1] = [None]
        self._size -= 1
        return True

    # get methods
    def getFront(self):
        if self._size == 0:  # queue is empty
            return -1
        return self._data[0]
    def getRear(self):
        if self._size == 0:  # queue is empty
            return -1
        return self._data[self._size - 1]

    # Check if Deque is full or empty
    def isEmpty(self):
        return self._size == 0
    def isFull(self):
        return not self._size == 0


if __name__ == '__main__':
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))
    print(circularDeque.insertLast(2))
    print(circularDeque.insertFront(3))
    print(circularDeque.insertFront(4))
    print(circularDeque.getRear())
    print(circularDeque.isFull())
    print(circularDeque.deleteLast())
    print(circularDeque.insertFront(4))
    print(circularDeque.getFront())
