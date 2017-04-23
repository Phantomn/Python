string = raw_input()
list = [0]*26

for i in string:
	list[ord(i)-ord("a")] += 1
for i in list:
	print "%d"%(i),
#print listt