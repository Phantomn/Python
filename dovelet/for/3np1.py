n = int(raw_input())
print n,

while n!=1:
	if n%2==0:
		print n/2,
		n /= 2
	else:
		print (n*3) + 1,
		n *= 3
		n += 1