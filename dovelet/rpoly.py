from math import *
r, n = map(float, raw_input().split())
n = int(n)

area = n/4*tan(pi/n)**-1

print "%.3f"%(area)