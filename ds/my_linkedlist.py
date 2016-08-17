class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.head = next


	def insert(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node