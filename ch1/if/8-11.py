print("(T)hursday, (F)riday, (S)aturday")
print("Input character(T,F,S) : ",end="")
ch=input()

if(ch=='T' or ch=='t'):
    print("Thursday")
elif(ch=='F' or ch=='f'):
    print("Friday")
elif(ch=='S' or ch=='s'):
    print("Saturday")
else:
    print("Input error")
