def LSearch(lst, length, target):
	for i in range(0,length):
		if lst[i] == target:
			return i
	return False

ar = [3,5,2,4,9]
idx = LSearch(ar, len(ar), 4)
if idx == False:
	print "Search Failed\n"
else:
	print "Target Saved Index : %d\n"%(idx)

idx = LSearch(ar, len(ar), 7)
if idx == False:
	print "Search Failed\n"
else:
	print "Target Saved Index : %d\n"%(idx)