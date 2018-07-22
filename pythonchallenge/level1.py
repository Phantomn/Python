def crypto(str):
	string = ""
	for i in str:
		if i >= 'a' and i <= 'z':
			string += chr(((ord(i) + 2) - ord('a')) % 26 + ord('a'))
		else:
			string += i
	print string


crypto("map")