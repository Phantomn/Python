# -*- coding: utf-8 -*-

class MyInt(int):
	pass


my_num = MyInt(5)


print dir(my_num.__class__)
