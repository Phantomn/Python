list = [0]*3

list[0], list[1], list[2] = map(int, raw_input().split())
for i in range(0,3):
	if list[i] > 1000:
		break
temp = 0
for i in range(0,3):
	for j in range(i,3):
		if list[i] > list[j]:
			list[i], list[j] = list[j], list[i]
print list[1]
