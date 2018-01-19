n = input()

if n%5==0:
	print n/5
else:
	if (n%5)%3 == 0:
		print (n/5)+(n%5)/3
	else:
		if (n%3) == 0:
			print n/3
		else:
			print -1
