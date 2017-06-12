print("Input Two integer : ",end="")
a,b=map(int,input().split())

if(a>b):
    print("Big number : %d"%(a))
elif(a<b):
    print("Big number : %d"%(b))
else:
    print("Two num is same")
