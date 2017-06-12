money = [[0 for col in range(2)]for row in range(2)]
for i in range(0,2):
	for j in range(0,1):
		money[i][j], money[i][j+1] = map(int, raw_input().split())


a = 1
b = 1

a = (money[0][1] - money[1][1]) / (money[0][0] - money[1][0])

b = money[0][1] - a*money[0][0]
print a, b