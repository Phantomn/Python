
def bin2dec(n):
	return str(int(str(n),2))
string = """01010111 01101000 01100001 01110100
01100001 01110010 01100101 01110100
01101000 01100101 01100110 01110101
01101100 01101100 01101110 01100001
01101101 01100101 01110011 01101111
01100110 01100101 01111000 01110000
01101100 01101111 01101001 01110100
01100001 01100010 01101100 01100101
01110110 01110101 01101100 01101110
01100101 01110010 01100001 01100010
01101001 01101100 01101001 01110100
01101001 01100101 01110011 01101001
01101110 01010111 01010000 01000001
00110010 00111111""".split()
print string
dec = []
for i in string:
	dec.append(bin2dec(i))

for i in dec:
	print chr(int(i)),