def max(x,y):
	if x>y:
		return x
	else:
		return y
def min(x,y):
	if x<y:
		return x
	else:
		return y

x,y = map(int, raw_input().split())

print "%d"%(max(min(x,y),x))