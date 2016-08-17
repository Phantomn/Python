def getChe1(num):
	count = 0
	list = [0 for i in range(num)]

	for i in range(2,num):
		list[i] = i

	for i in range(2,num):
		for j in range(2,num):
			if list[j] != i and list[j]%i==0:
				list[j] = 0

	for i in range(2,num):
		if list[i] != 0:
			count += 1
			print list[i],
			if count%5==0:
				print


getChe1(100)