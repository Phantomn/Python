r,e,c = map(int,raw_input().split())


e = e - c

if e>r:
	print "advertise"
elif e<r:
	print "do not advertise"
elif e==r:
	print "does not matter"