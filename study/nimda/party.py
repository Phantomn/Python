l,p = map(int, raw_input().split())
space = [0]*5
space = map(int, raw_input().split())

area = l*p

print "%d %d %d %d %d"%(space[0]-area, space[1]-area, space[2]-area, space[3]-area, space[4]-area)