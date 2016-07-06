h,m,s = map(int, raw_input().split())
cook_sec = input()
sec = cook_sec
d = 0
while sec > 0:
	if sec >= 3600:
		h += cook_sec/3600
		sec = sec % 3600 # 13

	else:
		m += cook_sec/60%60
		sec = sec % 60

		s += cook_sec%60
		sec = sec / 60

	while h>=24 or s/60 != 0 or m/60 != 0:
		if s >= 60:
			m += 1
			s %= 60
		elif m >= 60:
			h += 1
			m %= 60
		elif h >= 24:
			d += 1
			h %= 24

print h,m,s