a, b = map(int, raw_input().split())

while a != 0 and b != 0:
	print "A + B = ",a+b
	print "A - B = ",a-b
	print "A * B = ",a*b
	print "A / B = ",a/b
	print "A %% B = ",a%b
	a, b = map(int, raw_input().split())
