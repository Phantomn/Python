life=52560000
adult=life-(60*24*365)*20
ciggaret=2;
left_life=life-adult
print("adult : %d"%(adult))
print("left life : %d"%(left_life))
for i in range(0,):
    left_life-=ciggaret

reduced_life=(((left_life/60)/24)/365)
print("reduced life : %d"%(reduced_life))
print("Living years : %d"%(((((life/60)/24)/365)-reduced_life-20)))
