def Fibo(n):

	print "Func Call param %d"%(n)

	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fibo(n-1) + Fibo(n-2)

Fibo(7)