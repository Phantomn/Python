 a, b, c = map(int, raw_input().split())
#10 20 30
#
if a > b:
	if a > c:
		if b > c:
			print b
		else:
			print c
	else:
		print c
elif b > c:

else:
	print a