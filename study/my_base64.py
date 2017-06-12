def encrypt(data):
	bn = ""
	for plain in data:
		bn += "0"*(8-len(bin(ord(plain)).split("b")[1])) + bin(ord(plain)).split("b")[1]
	outlist = []
	bn += "0"*(6-len(bn)%6)

	for i in range(0, len(bn), 6):
		out = ""
		for j in range(i,i+6):
			out += bn[j]
		outlist.append(out)

	print "enc outlist", outlist
	dict = []

	for n in range( ord("A"), ord("Z")):
		dict.append(chr(n))
	for n in range( ord("a"), ord("z")):
		dict.append(chr(n))
	for n in range( 0, 10):
		dict.append(str(n))
	dict.append(["+", "/"])

	'''for n in range(0, len(dict)):
		print "%d "%(n),
		print dict[n]
	'''


	encoded = ""
	for i in outlist:
		print int(i,2),
	print
	for binary in outlist:
		encoded += (dict[int(binary, 2)])

	encoded += "=" * ((4- len(encoded) %4 )%4)

	return encoded


def decrypt(data):
	bn = ""
	for plain in data:
		bn += "0"*(8-len(bin(ord(plain)).split("b")[1])) + bin(ord(plain)).split("b")[1]
	outlist = []
	bn += "0"*(6-len(bn)%6)

	for i in range(0, len(bn), 6):
		out = ""
		for j in range(i,i+6):
			out += bn[j]
		outlist.append(out)

	print "enc outlist", outlist
	dict = []

	dict.append(["+", "/"])
	for n in range( 1, 11):
		dict.append(str(n))
	for n in range( ord("a"), ord("z")):
		dict.append(chr(n))
	for n in range( ord("A"), ord("Z")):
		dict.append(chr(n))



	'''for n in range(0, len(dict)):
		print "%d "%(n),
		print dict[n]
	'''


	decoded = ""
	for i in outlist:
		print int(i,2),
	print
	for binary in outlist:
		decoded += (dict[int(binary, 2)])

	decoded += "=" * ((4- len(decoded) %4 )%4)

	return decoded
'''def decrypt(data):
	bn = ""
	for plain in data:
		bn += bin(ord(plain)).split("b")[1]

	outlist = []
	bn += "0"*(8-len(bn)%8)

	for i in range(0, len(bn), 8):
		out = ""
		for j in range(i,i+8):
			out += bn[j]
		outlist.append(out)

	print outlist

	for i in range(0, len(outlist)):
		print int(outlist[i],2),
	print

	for i in range(0, len(outlist)):
		print chr(int(outlist[i],2)),
	print
'''




text = raw_input("Input Text : ")
print "Plain Text : %s"%(text) # aaaa
dec = encrypt(text)
print "Encrypted Base 64 Text : %s"%(dec) # YWFhYQ==

print "Decrypted Base 64 Text : %s"%(decrypt(dec))

















'''def decrypt(data):
	bn = ""
	for enc in data:
		#"0"*(8-len(bin(ord(enc)).split("b")[1])) +
		bn += bin(ord(enc)).split("b")[1]

	outlist = []
	bn += "0"*((8-len(bn)%8)%8)
	#print bn
	for i in range(0, len(bn), 8):
		out = ""
		for j in range(i,i+8):
			out += bn[j]
		outlist.append(out)


	print "dec outlist", outlist

	#decoded -= "=" * ((4- len(decoded) %4 )%4)
	dict = []

	for n in range( ord("A"), ord("Z")+1):
		dict.append(chr(n))
	for n in range( ord("a"), ord("z")+1):
		dict.append(chr(n))
	for n in range( 0, 10):
		dict.append(str(n))
	dict.append(["+", "/"])

	for i in dict:
		print i,
	print ""

	decoded = ""
	for binary in outlist:
		print chr(int(binary,2)),

		#decoded += (dict[int(binary, 2)])

	#return decoded'''