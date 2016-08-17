h,m = map(int , raw_input().split())
# 12 35
# 11 50

if m >= 45:
	m -= 45
else:
	if h > 0:
		h -= 1
		m += 60 - 45
	else:
		h += 24 - 1
		m += 60 - 45

print h, m