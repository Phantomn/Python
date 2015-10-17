print("Input hour minite second : ",end="")
h,m,s=map(int,input().split())

to_mid=0

to_mid+=h*3600
to_mid+=m*60
to_mid+=s

print("now midnight from %d second after"%(to_mid))

