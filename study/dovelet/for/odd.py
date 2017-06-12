list = [0 for i in range(7)]

for i in range(0,7):
	list[i] = int(raw_input())

odd_sum = 0
odd = []
for i in range(0,7):
	if list[i]%2==1:
		odd_sum += list[i]
		odd.append(list[i])
if odd_sum != 0:
	min = odd[0]
	for i in range(0,len(odd)):
		if min > odd[i]:
			min = odd[i]

if odd_sum == 0:
	print -1
else:
	print odd_sum
	print min