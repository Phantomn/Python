x=3
y=5
z=3
k=2
a=0

a = x<y|x<z&z<k
print("result a : %d"%(a))
a = (x<y|x<z)&z<k
print("result a : %d"%(a))
