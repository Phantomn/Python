posi = [[0]*4 for i in range(3)]

posi = [['Wide Receiver', 4.5, 150, 200],
		['Lineman',		 6.0, 300, 500],
		['Quarterback',	 5.0, 200, 300]]
speed, kg, power = map(float, raw_input().split())
hasposition = False

if speed <= 4.5 and kg >= 150 and power >= 200:
	print posi[0][0],
	hasposition = True
if speed <= 6.0 and kg >= 300 and power >= 500:
	print posi[1][0],
	hasposition = True
if speed <= 5.0 and kg >= 200 and power >= 300:
	print posi[2][0]
	hasposition = True

if hasposition == False:
	print "No positions"

#4.4 205 350
