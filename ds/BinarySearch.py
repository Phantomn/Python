def BSearch(lst, length, target):
	first = 0
	last = length - 1

	while first <= last:
		mid = (first+last) / 2

		if target == lst[mid]:
			return mid
		else:
			if target < lst[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return False

arr = [1,3,5,7,9]

idx = BSearch(arr, len(arr), 7)
if idx == False:
	print "Search Failed\n"
else:
	print "Target Saved Index : %d\n"%(idx)

idx = BSearch(arr, len(arr), 4)
if idx == False:
	print "Search Failed\n"
else:
	print "Target Saved Index : %d\n"%(idx)