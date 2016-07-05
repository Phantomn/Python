class Person:
	def __init__(self, name):
		self.name = name
	def say_hi(self):
		print 'Hello, my name is %s'%(self.name)
p = Person('Phantom')
p.say_hi()