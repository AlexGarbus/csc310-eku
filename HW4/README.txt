=========
PROGRAM 1
=========
This program allows for the implementation of the MyCircularDeque class.
This class creates a circular double-ended queue (deque).
A new deque is constructed using MyCircularDeque(k), where k is the maximum size of the deque.
Once the deque is created, the user may call the following methods:
	>insertFront(x): Adds x to the front end (left) of the deque.
		Returns whether the operation was successful.
	>insertFront(x): Adds x to the rear end (right) of the deque. 
		Returns whether the operation was successful.
	>deleteFront(): Deletes the element at the front end (left) of the deque.
		Returns whether the operation was successful.
	>deleteLast(): Deletes the element at the rear end (right) of the deque.
		Returns whether the operation was successful.
	>getFront(): Returns the element at the front end (left) of the deque.
		Returns -1 if the deque is empty.
	>getRear(): Returns the element at the rear end (right) of the deque.
		Returns -1 if the deque is empty.
	>isEmpty(): Returns whether the deque is empty.
	>isFull(): Returns whether the deque is full.

=========
PROGRAM 2
=========
This program allows for the implementation of the LinkedList class.
This class creates a linked list. A new linked list is constructed using LinkedList().
Once the linked list is created, the user may call the following methods:
	>insertTail(x): Inserts object x at the tail end of the list.
	>removeHead(): Removes and returns the element at the head of the list.
	>isEmpty(): Returns whether the list is empty.
	>splice(l1, l2): Sets this list to be a combination of the elements of l1 and l2.
		The elements of the spliced list will be in ascending order,
		as long as l1 and l2 are in ascending order.
		This method only works for empty lists.
		A string containing the elements of the new list is returned.
		l1 and l2 will be empty after this method's execution.

=========
PROGRAM 3
=========
This program allows for the implementation of the LinkedQueue class.
This class creates a linked list that functions as a queue.
A new linked queue is constructed using LinkedQueue().
Once the linked queue is created, the user may call the following methods:
	>enqueue(x): Inserts object x at the tail end of the queue.
	>dequeue(): Removes and returns the element at the head of the queue.
	>first(): Returns the element at the head of the queue without removing it.
	>len(): Returns the size of the queue.
	>isEmpty(): Returns whether the queue is empty.
	>search(x): Returns True if object x is in the queue.
		Returns False otherwise.