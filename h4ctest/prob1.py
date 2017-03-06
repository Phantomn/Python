'''list = map(int, raw_input().split())

max = list[0]
for i in range(0,len(list)-1):
	#for j in range(i,len(list)-1):
	if list[i] > max:
		max = list[i]

print max
'''

n = input()

for i in range(n, 0 , -1):
	for j in range(i, n+1):
		print "*",
	print