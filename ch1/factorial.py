print("Input num : ",end="")
n=int(input())
fac=0
for i in range(n,-1, -1):
    fac += n*(n-1)

print("%d! is %d"%(n,fac))
