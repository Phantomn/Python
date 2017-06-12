def BSearchRecur(lst, first, last, target):
	if first > last:
		return False
	mid = (first+last) / 2

	if lst[mid] == target:
		return mid
	elif target < lst[mid]:
		return BSearchRecur(lst, first, mid-1, target)
	else:
		return BSearchRecur(lst, mid+1, last, target)

ar = [1,3,5,7,9]

idx = BSearchRecur(ar, 0, len(ar), 7)
if idx == False:
	print "Search Failed"
else:
	print "Target Saved Index: %d"%(idx)
idx = BSearchRecur(ar, 0, len(ar), 4)
if idx == False:
	print "Search Failed"
else:
	print "Target Saved Index: %d"%(idx)