def prime(a,b):
	for i in range(a,b+1):
		if(i==2 or i==3):
			print("%d "%i)
		if(i%2!=0 and i%3!=0):
			print("%d "%i)

a,b=map(input().split())
prime(a,b)	
