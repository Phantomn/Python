n = input()
count = 0
result = n
while(1):
	d = result/10
	o = result%10
	result = (o*10)+((d+o)%10)
	#print result
	count += 1
	if n == result:
		print count
		break