class SortedPriorityQueue:

    ### Nested class ###
    class _Item:
        __slots__ = '_key', '_value'

        # Constructor
        def __init__(self, k, v):
            self._key = k
            self._value = v

        # Less than check
        def __lt__(self, other):
            return self._key < other._key

    ####################

    # Constructor
    def __init__(self):
        self._data = list()

    # Add a new key-value pair
    def insert(self, key, value):
        newest = self._Item(key, value)
        walk = len(self._data-1)
        ## TODO FIX THIS SHIT

        while walk > 1 and newest < self._data(walk): # Look for smaller key
            walk = self._data.before(walk)
        if walk == 0:    # Insert new key at start
            self._data.insert(newest, 0)
        else:   # Insert new key after walk
            self._data.add_after(walk, newest)

    # Return whether data is empty
    def isEmpty(self):
        return len(self._data) == 0

    # Remove and return item with minimum key
    def removeMin(self):
        if self.isEmpty:
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)



if __name__ == '__main__':
    queue = SortedPriorityQueue()
    queue.insert('A', 7)
    queue.insert('B', 4)
    queue.insert('C', 8)
    queue.insert('D', 2)
    queue.insert('E', 5)
    queue.insert('F', 3)
    queue.insert('G', 9)
    print(queue.removeMin()._value)
    print(queue.removeMin()._value)
    print(queue.removeMin()._value)
    print(queue.removeMin()._value)
    print(queue.removeMin()._value)
    print(queue.removeMin()._value)
    print(queue.removeMin()._value)