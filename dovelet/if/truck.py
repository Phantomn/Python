truck = 168

fir,sec,thr = map(int, raw_input().split())

if fir<=168:
	print "CRASH %d"%(fir)
elif sec<=168:
	print "CRASH %d"%(sec)
elif thr<=168:
	print "CRASH %d"%(thr)
else:
	print "NO CRASH"
