for i in range(4, 0, -1):
    for j in range(4, i, -1):
        print(" ",end="")
    for k in range(0, i):
        print("*",end="")
    for l in range(0, k):
        print("*",end="")
    print("\n")
