def Factorial(n):
	if n == 0:
		return 1
	else:
		return n * Factorial(n-1)

for i in range(1,6):
	print "%d! = %d"%(i,Factorial(i))