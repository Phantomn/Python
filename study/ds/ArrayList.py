class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.head = next

	def print_list(self):
		temp = self.head
		while temp:
			print temp.data,
			print "->",
			temp = temp.next
		print "None"

	def insert(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def delete(self, data):
		print "delete ",data
		cur = self.head
		found = False
		prev = None

		while cur != None and found is False:
			if cur.data == data:
				found = True
			else:
				prev = cur
				cur = cur.next

		if cur is None:
			print "Not Found"
		elif prev == None:
			self.head = cur.next
		else:
			prev.next = cur.next

	def search(self, data):
		temp = self.head
		found = False

		while temp and found is False:
			if temp.data == data:
				found = True
			else:
				temp = temp.next

		if found:
			print "found", temp.data
		else:
			print "Not Found"
list = Node()

list.insert(1)
list.insert(2)
list.insert(3)
list.print_list()
