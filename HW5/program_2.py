class BinaryTree:

    # ----------------------- Nested class -----------------------
    class _Node:
        __slots__ = '_left', '_right', '_element', '_parent', '_rank'

        # Node constructor
        def __init__(self, e, p):
            self._left = None
            self._right = None
            self._element = e
            self._parent = p

    # Constructor
    def __init__(self, e):
        self._root = self._Node(e[0], None)     # Set root node
        for i in range(1, len(e)):   # Add nodes
            self.add(e[i], self._root)

    # Adds a node by iteratively searching for an empty space
    def add(self, v, p):
        if p._parent is not None: #DEBUG
            print(str(p._element) + " " + str(p._parent._element))
        else:
            print(str(p._element))

        if v < p._element:
            if p._left is not None:
                self.add(v, p._left)
            else:
                p._left = self._Node(v, p)
        else:
            if p._right is not None:
                self.add(v, p._right)
            else:
                p._right = self._Node(v, p)

    # Perform inorder traversal and print the results
    def inorder(self, p):
        if p is not None:
            self.inorder(p._left)
            sys.stdout.write(str(p._element) + " ") # Print element
            self.inorder(p._right)

    # Perform preorder traversal and print the results
    def preorder(self, p):
        sys.stdout.write(str(p._element) + " ") # Print element
        if p._left is not None:
            self.preorder(p._left)
        if p._right is not None:
            self.preorder(p._right)

import sys

if __name__ == '__main__':
    #elements = [1, None, 2, 3]
    elements = [1, 2, 3, 4, 5, 6, 7]
    tree = BinaryTree(elements)

    # Print inorder
    sys.stdout.write("inorder: ")
    tree.inorder(tree._root)
    print("")

    # Print preorder
    sys.stdout.write("preorder: ")
    tree.preorder(tree._root)
    print("")