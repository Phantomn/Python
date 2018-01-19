a = []
b = []
while True:
	c, d = map(int, raw_input().split())
	if c != 0 and d != 0:
		a.append(c)
		b.append(d)
	else:
		break

for i in range(0,len(a)):
	print "%d"%(a[i]+b[i])