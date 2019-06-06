testcase = input()
case = []*testcase
for i in range(0, testcase):
	data = raw_input().split(' ')
	case.append(data[0])
	string = [[]*len(data[1])]*testcase
	for j in range(0, len(data[1])):
		string[i][j].append(data[1][j])

print string
for i in range(0, int(case[i])):
	for j in range(0, int(case[i])):
		print string[i],