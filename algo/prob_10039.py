n = [0]*5
sum = 0
for i in range(0,5):
	data = input()
	if data < 40:
		n[i] = 40
	else:
		n[i] = data
	sum += n[i]
print sum/5