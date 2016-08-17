# coding: utf-8
y, m, d = map(int, raw_input().split())

if (y+m+d)%10!=0:
	print "노력하세요!"
else:
	print "운수대통!"