import sys

price = [0]*9
unknown = input()
if unknown >= 10000:
	sys.exit()

for i in range(0,9):
	price[i] = input()
	if price[i] >= 10000:
		sys.exit()
sums = 0
for i in range(0,9):
	sums += price[i]

print abs(sums-unknown)