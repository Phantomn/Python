a = input()
b = input()
b_hun = b/10/10
b_ten = b/10%10
b_one = b%10

print "%d\n%d\n%d\n%d\n"%(a*b_one,a*b_ten,a*b_hun,a*b)