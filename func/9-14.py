def factorial(n):
    if(n<=1):
        return 1
    else:
        return n*factorial(n-1)

print("Input integer : ",end="")
a=int(input())
result=factorial(a)
print("%d factorial is %d"%(a,result))
