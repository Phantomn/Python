print("Input binary : ",end="")
binary=int(input())
f=int((binary/1000))
t=int(((binary%1000)/100))
s=int((((binary%1000)%100)/10))
o=int((((binary%1000)%100)%10))

decimal=int((f*8)+(t*4)+(s*2)+(o*1))
print(int('1111',10))
print("binary %d is decimal %d"%(binary,decimal))
