def Recursive(num):
	if num <= 0:
		return
	print "Recursive call! %d"%(num)
	Recursive(num-1)

Recursive(3)