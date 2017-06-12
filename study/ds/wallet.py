class wallet:
	def __init__(self, coin100Num, bill5000Num):
		self.coin100Num = coin100Num
		self.bill5000Num = bill5000Num

	def TakeOutMoney(pw, coinNum, billNum):
		coin100Num -= coinNum
		bill5000Num -= billNum
		return coinNum + billNum
	def PutMoney(pw, coinNum, billNum):
		coin100Num += coinNum
		bill5000Num += billNum