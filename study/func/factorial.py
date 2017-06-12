print("Input num : ",end="")
n=int(input())
fac=1
def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)
fac=factorial(n)
print("%d! is %d"%(n,fac))
