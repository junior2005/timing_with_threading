'''
Author: Nicholas Theisen
KUID: 3124859
Date: 12/07/2024
Lab: lab9
Last modified: 12/07/2024
Purpose: Contains all data structures used for timing
'''

class Node:
	def __init__(self, entry):
		self.entry = entry
		self.next = None

class BinaryNode:
	def __init__(self, entry):
		self.entry = entry
		self.left = None
		self.right = None

class Stack:
	def __init__(self):
		self._top = None

	def push(self, entry):
		temp = Node(entry)
		temp.next = self._top
		self._top = temp

	def pop(self):
		temp = self._top
		if self.is_empty():
			raise RuntimeError("Stack Is Empty.")
		else:
			self._top = self._top.next
		return temp.entry

	def peek(self):
		if self.is_empty():
			raise RuntimeError("Stack Is Empty.")
		return self._top.entry

	def is_empty(self):
		return self._top is None

class LinkedQueue:
	def __init__(self):
		self._front = None
		self._back = None

	def is_empty(self):
		return self._front is None 

	def enqueue(self, entry):
		temp = Node(entry)
		if self.is_empty():
			self._front = temp
			self._back = temp
		else:
			self._back.next = temp
			self._back = temp

	def dequeue(self):
		temp = self._front
		if self.is_empty():
			raise RuntimeError("Queue is Empty.")
		
		self._front = self._front.next
		if self._front is None:
			self._back = None
		return temp.entry

	def peek_front(self):
		if self.is_empty():
			raise RuntimeError("Queue is Empty.")
		else:
			return self._front.entry

class LinkedList:
	def __init__(self):
		self._front = None
		self._length = 0

	def clear(self):
		self._front = None
		self._length = 0

	def length(self):
		return self._length

	def get_entry(self, index):
		if (index >= self._length) or (index < 0):
			raise IndexError("Index out of bounds.")
		else:
			jumper = self._front
			for i in range(index):
				jumper = jumper.next
			
			return jumper.entry

	def insert(self, index, entry):
		if (index < 0) or (index > self._length):
			raise IndexError
		
		elif index == 0:
			temp = Node(entry)
			temp.next = self._front
			self._front = temp

		else:
			temp = Node(entry)
			jumper = self._front
			for i in range(index - 1):
				
				if jumper.next is None:
					raise IndexError
				jumper = jumper.next
			temp.next = jumper.next
			jumper.next = temp
		self._length += 1

	def remove(self, index):
		if (index < 0) or (index > self._length - 1):
			raise IndexError

		elif index == 0:
			self._front = self._front.next

		else:
			jumper = self._front
			for i in range(index - 1):
				jumper = jumper.next

			jumper.next = jumper.next.next
		self._length -= 1

	def set_entry(self, index, entry):
		if (index < 0) or (index > self._length - 1):
			raise RuntimeError
		else:
			jumper = self._front
			for i in range(index):
				jumper = jumper.next
			jumper.entry = entry

class MaxHeap:
	def __init__(self):
		self._heap = []

	def peek(self):
		if len(self._heap) > 0:
			return self._heap[0]
		else:
			raise RuntimeError("Heap empty.")
	
	def add(self, entry):
		self._heap.append(entry)
		self._upheap(len(self._heap) - 1)
	
	def remove(self):
		if len(self._heap) > 0:
			root_val = self._heap[0]
			self._heap[0] = self._heap[-1]
			self._heap.pop()
			self._downheap(0)
			return root_val
		else:
			raise RuntimeError("Heap empty.")
	
	def _upheap(self, index):
		if index == 0:
			return

		parent_index = self.parent(index)

		if self._heap[index] < self._heap[parent_index]:
			return 
		temp = self._heap[parent_index] 
		self._heap[parent_index] = self._heap[index] 
		self._heap[index] = temp 
		self._upheap(parent_index)

	def _downheap(self, index):
		lc = self.left(index)
		rc = self.right(index)

		if lc >= len(self._heap):
			return
		if rc >= len(self._heap):
			largest = lc
		else:
			largest = lc if self._heap[lc] > self._heap[rc] else rc

		if self._heap[index] >= self._heap[largest]:
			return	
		temp = self._heap[largest]
		self._heap[largest] = self._heap[index]
		self._heap[index] = temp

		self._downheap(largest)

	def parent(self, index):
		return (index - 1)//2

	def left(self, index):
		return (2 * index) + 1

	def right(self, index):
		return (2 * index) + 2
	

class BinarySearchTree:
	def __init__(self):
		self._root = None

	def add(self, item):
		self._root = self._rec_add(item, self._root)

	def preorder(self, visit_function):
		"""Pre order traversal: Visit, LST, RST"""
		self._rec_preorder(visit_function, self._root)

	def inorder(self, visit_function):
		"""In order traversal: LST, Visit, RST"""
		self._rec_inorder(visit_function, self._root)

	def postorder(self, visit_function):
		"""Post order traversal: LST, RST, Visit"""
		self._rec_postorder(visit_function, self._root)

	def search(self, key):
		return self._rec_search(key, self._root)

	def remove(self, key):
		self._root = self._rec_remove(key, self._root)

	def deep_copy(self):
		new_tree = BinarySearchTree()
		new_tree._root = self._rec_deep_copy(self._root)
		return new_tree

	def _rec_add(self, item, cur_node):
		if cur_node is None:
			return BinaryNode(item)

		if cur_node.entry == item:
			raise ValueError('No Duplicates Allowed.')
			
		elif cur_node.entry > item:
			cur_node.left = self._rec_add(item, cur_node.left)

		else:
			cur_node.right = self._rec_add(item, cur_node.right)
		return cur_node

	def _rec_preorder(self, visit_function, cur_node):
		if cur_node is None:
			return None
		visit_function(cur_node.entry)
		self._rec_preorder(visit_function, cur_node.left)
		self._rec_preorder(visit_function, cur_node.right)

	def _rec_inorder(self, visit_function, cur_node):
		"""Hidden recursive in order traversal method"""
		if cur_node is None:
			return None
		self._rec_inorder(visit_function, cur_node.left)
		visit_function(cur_node.entry)
		self._rec_inorder(visit_function, cur_node.right)

	def _rec_postorder(self, visit_function, cur_node):
		if cur_node is None:
			return None
		self._rec_postorder(visit_function, cur_node.left)
		self._rec_postorder(visit_function, cur_node.right)
		visit_function(cur_node.entry)

	def _rec_search(self, key, cur_node):
		if cur_node is None:
			raise KeyError(f'Key: {key} not found.')
		if cur_node.entry == key:
			return cur_node.entry
		elif cur_node.entry > key:
			return self._rec_search(key, cur_node.left)
		else:
			return self._rec_search(key, cur_node.right)

	def _rec_remove(self, key, cur_node):
		if cur_node is None:
			raise KeyError(f'Key: {key} not found.')
		if cur_node.entry > key:
			cur_node.left = self._rec_remove(key, cur_node.left)

		elif cur_node.entry < key:
			cur_node.right = self._rec_remove(key, cur_node.right)

		else:
			if cur_node.right is None:
				return cur_node.left
			if cur_node.left is None:
				return cur_node.right
			else:
				max_left = self._max_value(cur_node.left)
				cur_node.left = self._rec_remove(max_left.entry, cur_node.left)
				cur_node.entry = max_left.entry
		return cur_node
		
	def _max_value(self, cur_node):
		while cur_node.right is not None:
			cur_node = cur_node.right
		return cur_node

	def _rec_deep_copy(self, cur_node):
		if cur_node is None:
			return None
		new_root = BinaryNode(cur_node.entry)
		new_root.left = self._rec_deep_copy(cur_node.left)
		new_root.right = self._rec_deep_copy(cur_node.right)
		return new_root
