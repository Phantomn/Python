print("Input 3 figure num : ",end="")
n=int(input())

h=int(n/100)
t=int((n%100)/10)
o=int((n%100)%10)

print("%d %d %d"%(h,t,o))
if(h%2==0):
    print("%d is even num "%(h))
else:
    print("%d is odd num "%(h))
if(t%2==0):
    print("%d is even num "%(t))
else:
    print("%d is odd num "%(t))

if(o%2==0):
    print("%d is even num "%(o))
else:
    print("%d is odd num "%(o))
print("")
