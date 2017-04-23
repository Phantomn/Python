num = raw_input()
list = num.split(" ")
for i in range(0,len(list)):
	for j in range(i, len(list)):
			if int(list[i]) < int(list[j]):
				list[i], list[j] = list[j], list[i]

print list[1]