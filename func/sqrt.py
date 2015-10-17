print("A TABLE OF POWERS")
print("------------------------------------------------------------------------")
print("INTEGER\t\tSQUARE\t\tCUBE\t\tQUARTIC\t\tQUINTIC ")
print("------------------------------------------------------------------------")
a=[0]*5
for i in range(1,11):
    for j in range(1,6):
        a[j-1]=pow(i,j)
    print("%8d\t%8d\t%8d\t%8d\t%8d"%(a[0],a[1],a[2],a[3],a[4]))


