def isdiv_mul(a,b):
	if a == 0:
		print "%d !| %d"%(a,b)
	elif b == 0:
		print "%d | %d"%(a,b)
	else:
		if b%a == 0:
			print "%d | %d"%(a,b)
		else:
			print "%d !| %d"%(a,b)


m,n = map(int, raw_input().split())
isdiv_mul(m,n)

# n = m * q
# n/m = q
# 2 32
# q = 16
# 32 0 32/0
# 0 = 0 * 0