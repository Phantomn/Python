a, b = map(int, raw_input().split())

def odd_even(num):
	dic = {0 : 'even', 1 : 'odd'}
	if num%2==1:
		return dic[1]
	else:
		return dic[0]

print "%s+%s=%s"%(odd_even(a),odd_even(b), odd_even(a+b))
print "%s*%s=%s"%(odd_even(a),odd_even(b), odd_even(a*b))
