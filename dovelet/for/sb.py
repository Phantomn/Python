strowberry = [0 for i in range(7)]


strowberry = map(int, raw_input().split())

max = strowberry[0]
for i in range(0, 7):
	for j in range(0,7):
		if strowberry[j] > max:
			max = strowberry[j]

print strowberry.index(max)+1