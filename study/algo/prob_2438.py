n = input()
str = ""
for i in range(0,n):
	for j in range(0,i+1):
		str += "*"
	str += "\n"
print str,