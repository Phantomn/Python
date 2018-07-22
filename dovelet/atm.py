x,y = map(float, raw_input().split())


if (x%5!=0 and y%5!=0):
	print "%.2f"%(y)
else:
	print x, y
	if x>=y or x == y:
		print "%.2f"%(y)
	else:
		y = y - x
		y = y - 0.5
		print "%.2f"%(y)