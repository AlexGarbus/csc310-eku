=========
PROGRAM 1
=========
This program implements the method SolveHanoi(n, towerA, towerB, towerC), 
which solves the Tower of Hanoi puzzle recursively.
n is the number of initial discs.
towerA, towerB, and towerC are the stacks representing each tower.
towerA must have n discs before the method is called, otherwise it won't work.

=========
PROGRAM 2
=========
This program implements the Node and BinaryTree classes.
BinaryTree contains a root Node connected to several child Nodes.
How to construct BinaryTree:
	-Create a new object using BinaryTree()
	-Create an array of Integers, where each Integer is a node of the tree
		>Array should be sorted by left to right, top to bottom
		>Null should be used for empty nodes
	-Call BinaryTree.insert(a), where a is the array of Integers
Once constructed, the user may call inorder() or preorder() to perform
inorder traversal and preorder traversal, respectively.