print("Input (unsinged in) : ",end="")
n=int(input())
count=0
print("%d's multiple : "%(n),end="")
for i in range(1,101):
    if(i%n==0):
        print("%d "%(i),end="")
        count+=1
print("\n")
print("%d's multiple number : %d"%(n,count))

