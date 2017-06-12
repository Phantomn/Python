n1=2
n2=3
n3=5
re1=0
re2=0
re3=0

re1=((n1>0) & (n2<10))
re2=((n2<=2) | (n3>5))
re3=(~n3)

print("result1 : %d"%(re1))
print("result2 : %d"%(re2))
print("result3 : %d"%(re3))
