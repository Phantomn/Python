def sum():
    tot=0
    num=0
    num=int(input())

    for i in range(1,num+1):
        tot+=i
    return tot

def output(x):
    print("result : %d"%x)
    return

print("---Program Start---")
print("Input integer : ",end="")
result=sum()
output(result)


