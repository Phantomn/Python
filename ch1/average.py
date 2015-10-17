tot=0
for i in range(0,10):
    print("Input score : ",end="")
    score=int(input())
    tot+=score

print("average is %.1lf"%(tot/10))
