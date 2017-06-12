class Node:
	def __init__(self, data=None, head=None):
		self.data = data


class LinkedList():
	def __init__(self, head=Node):
		self.head = None

	def insert(self, data):
		new_node = Node(data)
		new_node.head = self.head
		self.head = new_node

	def delete(self, data):
		cur = self.head
		found = False
		prev = None

		while cur != None and found is False:
			if cur.data == data :
				found = True
			else:
				prev = cur
				cur = cur.head
		if cur is None:
			print "Not Found"
		elif prev == None:
			self.head = cur.head
		else:
			prev.head = cur.head

	def search(self, data):
		temp = self.head
		found = False

		while temp and found is False:
			if temp.data == data :
				found = True
			else:
				temp = temp.head
		if found:
			print "Found", temp.data
		else:
			print "Not Found"

	def print_list(self):
		temp = self.head
		while temp:
			print temp.data,
			print "->",
			temp = temp.head
		print "None"


list = LinkedList()

list.insert(1)
list.insert(2)

list.print_list()