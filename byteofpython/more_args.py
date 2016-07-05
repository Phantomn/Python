def powersum(power, *args):
	'''Return the sum of each argument raised to the specified power.'''
	tot = 0
	for i in args:
		print args
		tot += pow(i, power)
		print tot
	return tot

powersum(2, 3, 4)

powersum(2, 10)