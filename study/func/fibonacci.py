def fibonacci(n):
    if(n<=1):
	if(n==1):
		print "f(1) = %d\n"%n,
        return n
    else:
        return fibonacci(n-1)+2 *fibonacci(n-2)

result=fibonacci(6)
print "%d "%result,
