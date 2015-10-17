def sum(n):
    sum=0

    for i in range(1,n+1):
        sum+=i
    return sum

print("Input number : ",end="")
a=int(input())
result=sum(a)
print("1 ~ %d's sum : %d"%(a,result))
