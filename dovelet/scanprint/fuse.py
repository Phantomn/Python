import math
DESKTOP = 1.5
MONITOR = 1.0
PRINTER = 2.0
ROUTER = 0.5

PC = DESKTOP + MONITOR


pc, printer, router = map(int,raw_input().split())

fuse = ((pc*PC+printer*PRINTER+router*ROUTER))*2

fuse = fuse / 10

print "%d amperes"%(math.ceil(fuse)*10)