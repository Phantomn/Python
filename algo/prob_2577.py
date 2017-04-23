a, b, c = map(int, raw_input().split())

result =  str(a*b*c)
count = [0]*10
for i in result:
	count[ord(i)-ord("0")] += 1
for i in count:
	print i,