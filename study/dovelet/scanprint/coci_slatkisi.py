mirko, unit = map(int, raw_input().split())

min = int(mirko/pow(10,unit))*pow(10,unit)
max = int(mirko/pow(10,unit)+1)*pow(10,unit)

value = mirko - min

if value<5*pow(10,unit-1):
	print min
else:
	print max