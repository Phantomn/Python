m = input()

for i in range(101, 1, -1):
	n = (i*(i+1))/2
	if n == m:
		print i
		break
