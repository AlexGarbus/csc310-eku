All 3 programs require the List and ArrayList utilities.

=========
PROGRAM 1
=========
This program implements the PriorityQueue class,
which allows for the insertion and sorting of Items.
Each Item in the PriorityQueue consists of a key and a value,
both of which are integers.
Once implemented, the following methods may be called:
	>insert(key, value) - Insert a new Item
	>removeMin() - Remove and return the minimum priority element

=========
PROGRAM 2
=========
This program implements methods for in-place heap-sort.
A heap should be represented by a list of integers,
where the index of each integer is its rank.
The program assumes that each internal node of the heap has 2 children,
with the exception of the parent of the rightmost external mode,
which will have 1 child if there are an odd number of nodes.
The InPlaceHeapSort method can then be called,
with the list as its argument.
The method will return the sorted list.

=========
PROGRAM 3
=========
This program implements the BinHeap class,
which allows for the storage and modification of a minimum binary heap.
The program assumes that each internal node of the heap has 2 children,
with the exception of the parent of the rightmost external mode,
which will have 1 child if there are an odd number of nodes.
Once implemented, the following methods may be called:
	>insert(key) - Insert a new item
	>find_min() - Return the minimum item
	>del_min() - Return and remove the minimum item
	>is_empty() - Return whether the heap is empty
	>size() - Return the number of items in the heap
	>build_heap(list) - Build a new heap out of a list of items
The following methods also may be called within the BinHeap class itself:
	>upheap - Moves an out-of-order item up the tree
	>downheap - Moves an out-of-order item down the tree
	>swap(x, y) - Swaps the items at indexes x & y
