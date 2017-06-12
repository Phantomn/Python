a=0
b=0
c=0
for i in range(0,3):
    if(a==0):
        print("Input : ",end="")
        a=int(input())
        continue
    if(b==0):
        print("Input : ",end="")
        b=int(input())
        continue
    if(c==0):
        print("Input : ",end="")
        c=int(input())
        continue
if(a>b):
    if(a>c):
        print("result : %d"%(a))
elif(b>c):
        print("result : %d"%(b))
elif(c>a):
    print("result : %d"%(c))
if(a==b):
    if(a>c):
        print("a and b is same result %d"%(a))
    else:
        print("a and b is same result %d"%(c))
if(b==c):
    if(b>a):
        print("b and c is same result %d"%(b))
    else:
        print("b and c is same result %d"%(c))
