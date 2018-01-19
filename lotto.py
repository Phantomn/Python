import random
import sys
print "---------------Lotto Generator---------------"

user = [0]*6
lotto = [0]*6
def generate():
	lotto = random.sample(range(1,47),5)
	lotto.sort()
	return lotto

def game(lotto,user):
	count = 0
	for i in range(0,5):
			for j in range(i,5):
				if lotto[i] == user[j]:
					count += 1

			if count == 5:
				print "5 Num all Same!!!!"
				print lotto, user
				count = 0
				return True
			elif count == 4:
				print "Second Grade!!\n4 Number is Same!!"
				print lotto, user
				count = 0
				return True
			elif count == 3:
				print lotto, user
				print "3 Number"
				count = 0
				return False
			elif count == 2:
				#print "2 Number"
				count = 0
				return False

print "Input Number : ",
user = map(int, raw_input().split())
user.sort()


grade = None
while grade != True:
	lotto = generate()
	grade = game(lotto,user)