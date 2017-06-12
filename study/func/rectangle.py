def getArea(x,y):
    return x*y

print("Input Length and height : ",end="")
a,b=map(int,input().split())
result=getArea(a,b)
print("Rectangle Area is %d"%result)
