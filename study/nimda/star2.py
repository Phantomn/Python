n = input()

for i in range(n, 0, -1):
	for j in range(0, i):
		print " ",
	for k in range(0, n):
		if k >= j:
			print "*",
	if i != 0:
		print