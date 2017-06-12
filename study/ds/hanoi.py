def HanoiTowerMove(num, A, B, C):
	if num == 1:
		print "plate 1 is %c from %c to move"%(A,C)
	else:
		HanoiTowerMove(num-1, A, C, B)
		print "plate %d is %c from %c to move"%(num,A,C)
		HanoiTowerMove(num-1, B, A, C)

HanoiTowerMove(30, 'A', 'B', 'C')

# 3 A B C -> 2 A C B -> 1 A B C -> !1 A C
# 2 A C B -> !2 A B -> 1 C A B -> !1 C B
# 3 A B C -> !3 A C -> 2 B A C -> 1 B C A -> !1 B A
# 2 B A C -> !2 B C -> 1 A B C -> !1 A C