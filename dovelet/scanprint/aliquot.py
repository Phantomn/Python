def issquare(n):
    return int(n ** 0.5) ** 2 == n

a,b = map(int, raw_input().split())
entire_num = b-a+1
for i in xrange(a,b+1):
	if issquare(i):
		entire_num -= 1
print entire_num