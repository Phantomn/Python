import sys
sum=0
cnt=0
def count():
    global cnt
    cnt+=1
    return cnt
def add():
    global cnt
    print("Input Two Num(0, 0 -> exit) : ",end="")
    a,b=map(int,input().split())
    if(a==0 and b==0):
        print("count : %d"%cnt)
        sys.exit()
    sum=a+b
    print("Add result : %d"%sum)
    cnt=count()


while True:
    add()

