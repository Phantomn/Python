import sys
count=0
sum=0
n=1
while(1):
    if(n==0):
        print("sum : %d, input count : %d"%(sum,count-1))
        sys.exit()
    print("Input number : ",end="")
    n=int(input())
    sum+=n
    count+=1
