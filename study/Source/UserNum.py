str = raw_input()
remove = 6
num = str[:remove] + str[remove+1:]
j = 2
key_num = 11
sum = 0
in_num = []
save = 0
for i in range(0, 12):
	save = int(num[i]) * j
	in_num.append(save)
	print num[i], j, save
	j += 1

	if j >= 10:
		j = 2

for i in range(0,12):
	sum += int(in_num[i])
print sum
div, mod = divmod(sum, key_num)
print "\n\n"

print div,mod