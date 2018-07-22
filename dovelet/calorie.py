list = [[0]*4 for i in range(4)]
list = [[461, 431, 420, 0],
		[130, 160, 118, 0],
		[100, 57, 	70, 0],
		[167, 266,  75, 0]]

sum = 0
'''print "3 burgers"
print " 1. Cheeseburger (461 C)"
print " 2. Fishburger (431 C)"
print " 3. Veggieburger (420 C)"
print " 4. No burger"

print "3 drinks"
print " 1. Soft Drink (130 C)"
print " 2. Orange Juice (160 C)"
print " 3. Milk (118 C)"
print " 4. No drink"

print "3 Side order"
print " 1. Fries (100 C)"
print " 2. Baked Potato (57 C)"
print " 3. Chef Salad (70 C)"
print " 4. No side order"

print "3 Desserts"
print " 1. Apple Pie (167 C)"
print " 2. Sundae (266 C)"
print " 3. Fruit Cup (75 C)"
print " 4. No dessert"'''
a,b,c,d = map(int, raw_input().split())
if a == 1:
	sum += 461
elif a == 2:
	sum += 431
elif a == 3:
	sum += 420
elif a == 4:
	sum += 0

if b == 1:
	sum += 130
elif b == 2:
	sum += 160
elif b == 3:
	sum += 118
elif b == 4:
	sum += 0

if c == 1:
	sum += 100
elif c == 2:
	sum += 57
elif c == 3:
	sum += 70
elif c == 4:
	sum += 0

if d == 1:
	sum += 167
elif d == 2:
	sum += 266
elif d == 3:
	sum += 75
elif d == 4:
	sum += 0
print "Your total Calorie count is %d."%(sum)