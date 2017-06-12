import math

a,b = map(int, raw_input().split())

even = (b - int(math.sqrt(b))) - (a-1 - int(math.sqrt(a-1)))

print even