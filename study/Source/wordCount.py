wc = raw_input().split(" ")
count = 0
#print wc
for i in range(0,len(wc)):
	if len(wc[i]) != 0:
		count += 1
print count