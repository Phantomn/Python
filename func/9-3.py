def divide(x,y):
    val=x/y
    return val
def output(x):
    print("divide result %lf"%x)
    return
def information():
    print("Program Start")
    return

information()
print("input first float : ",end="")
n1=float(input())
print("input second float : ",end="")
n2=float(input())

result=divide(n1,n2)
output(result)
