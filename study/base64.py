def encrypt(plain):
	bn = ""
	for text in plain:
		bn += ("0" * (8-len((bin(ord(text)).split("b")[1]))) + bin(ord(text)).split("b")[1])
	out = []
	bn += "0"*(6-len(bn)%6)
	out += [bn[i:i+6] for i in range(0, len(bn), 6)] # string -> ascii -> 8bit

	dict = []
	for n in range( ord("A"), ord("Z")+1 ):
		dict.append(chr(n))
	for n in range( ord("a"), ord("z")+1 ):
		dict.append(chr(n))
	for n in range( 0, 10 ):
		dict.append(str(n))
	dict.append(["+", "/"])

	encoded = ""
	for binary in out:
		encoded += (dict[int(binary, 2)])

	encoded += "=" * ((4 - len(encoded)%4)%4)

	return encoded

'''def decrypt(plain):
# Y  		   W  			F  			h   		Y  			Q  			==
#01011001   01010111 	01000110    01101000 	01011001 	01010001    00000000
	bn = ""
	for text in plain:
		bn += (bin(ord(text)).split("b")[1]) + bin(ord(text)).split("b")[1])
	out += [bn[i:i+8] for i in range(0, len(bn), 8)]

	return out
	'''

data = raw_input("Encrypt Code in Base 64 : ")

print "Plain Text : %s"%(data)
print "Encrypted Base 64 Text : %s"%(encrypt(data))
#print "Decrypted Plain Text : %s"%(decrypt(encrypt(data)))