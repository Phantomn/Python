class Foo(object):
	pass

class Bar(Foo):
	pass

print dir(Foo.__subclasses__())
