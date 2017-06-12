def abss(n):
    if(n<0):
        return -n
    elif(n>0):
        return n
    else:
        return 0

print("Input : ",end="")
a=int(input())
print("%d abs is %d"%(a,abss(a)))
