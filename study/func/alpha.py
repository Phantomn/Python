def alpha():
    L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    print("Input alphabet : ",end="")
    a=input()
    for i in L:
        result=L.find(a)
    print("%s is %d's alphabet"%(a,result))
alpha()
