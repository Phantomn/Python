a,b = map(int, raw_input().split())

q,r = divmod(a,b)
print "%d %d"%(q,r)