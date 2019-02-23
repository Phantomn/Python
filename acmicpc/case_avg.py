count = input()
lst = [0]*count
for i in range(0, count):
	num = map(int , raw_input().split(' '))
	lst[i] = [0]*num[0]
	for j in range(0, num[0]):
		lst[i][j] = num[j+1]
avg = [0.0]*len(lst)
case_sum = 0
over = 0
for i in range(0, len(lst)):
	case_sum = 0
	for j in range(0, len(lst[i])):
		case_sum += lst[i][j]
	avg[i] = float(case_sum/(len(lst[i])))

for i in range(0, len(lst)):
	case_sum = 0
	over = 0
	for j in range(0, len(lst[i])):
		if avg[i] < lst[i][j]:
			over += 1
	#print over, len(lst[i]),
	print "%.3f%%"%((float(over)/len(lst[i]))*100)