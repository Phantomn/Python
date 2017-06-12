print("Input three num : ",end="")
a,b,c=map(int,input().split())


if(a>b):
    if(a>c):
        print("a is bigger : %d"%(a))
elif(b>c):
    print("b is bigger : %d"%(b))
elif(c>a):
    print("c is bigger : %d"%(c))
