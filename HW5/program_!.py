class Stack:

    # Constructor
    def __init__(self):
        self._data = []

    # Push element e onto stack
    def push(self, e):
        self._data.append(e)

    # Remove and return top element of stack
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self._data.pop()

    # Check if empty
    def isEmpty(self):
        return len(self._data) == 0


class TowersOfHanoi:

    # Constructor
    def __init__(self):
        self._pegA = Stack()
        self._pegB = Stack()
        self._pegC = Stack()

    # Solve the Towers of Hanoi puzzle recursively
    def solve(self, n, a, b, c):
        if self._pegA.isEmpty() and self._pegB.isEmpty() and self._pegC.isEmpty():  # Create disks if there are none
            for i in range(n, 1):
                self._pegA.push(i)
        else:   # Print current move
            print("Move disk " + n + " from peg " + a + " to peg " + b)
        if n == 1:  # Base case
            return
        else:   # Recursive calls
            self.solve(n-1, a, c, b)
            self.solve(1, a, b, c)
            self.solve(n-1, b, a, c)


if __name__ == '__main__':
    T = TowersOfHanoi()
    T.solve(2, "A", "B", "C")
