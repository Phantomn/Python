n = input()
a = []
b = []
for i in range(0,n):
	c, d = map(int, raw_input().split(","))
	a.append(c)
	b.append(d)

for i in range(0,n):
	print "%d"%(a[i]+b[i])