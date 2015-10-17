def plus(i,j):
    return i+j
def minus(i,j):
    return i-j
def mul(i,j):
    return i*j
def div(i,j):
    return float(i/j)

print("Input Two int : ",end="")
a,b=map(int,input().split())
result=plus(a,b)
print("%d + %d = %d"%(a,b,result))
result=minus(a,b)
print("%d - %d = %d"%(a,b,result))
result=mul(a,b)
print("%d * %d = %d"%(a,b,result))
result=div(a,b)
print("%d / %d = %.2lf"%(a,b,result))
