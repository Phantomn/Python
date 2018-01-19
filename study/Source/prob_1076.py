listd = ['']*3
for i in range(0,3):
	listd[i] = raw_input()
cnt = 0
result = []
while cnt < 3:
	if cnt < 2:
		if listd[cnt] == 'black':
			result += ''.join('0')
			cnt += 1
			continue
		elif listd[cnt] == 'brown':
			result += ''.join('1')
			cnt += 1
			continue
		elif listd[cnt] == 'red':
			result += ''.join('2')
			cnt += 1
			continue
		elif listd[cnt] == 'orange':
			result += ''.join('3')
			cnt += 1
			continue
		elif listd[cnt] == 'yellow':
			result += ''.join('4')
			cnt += 1
			continue
		elif listd[cnt] == 'green':
			result += ''.join('5')
			cnt += 1
			continue
		elif listd[cnt] == 'blue':
			result += ''.join('6')
			cnt += 1
			continue
		elif listd[cnt] == 'violet':
			result += ''.join('7')
			cnt += 1
			continue
		elif listd[cnt] == 'grey':
			result += ''.join('8')
			cnt += 1
			continue
		elif listd[cnt] == 'white':
			result += ''.join('9')
			cnt += 1
			continue
	if cnt == 2:
		if listd[cnt] == 'black':
			result += ''.join('')
			cnt += 1
			continue
		elif listd[cnt] == 'brown':
			result += ''.join('0')
			cnt += 1
			continue
		elif listd[cnt] == 'red':
			result += ''.join('00')
			cnt += 1
			continue
		elif listd[cnt] == 'orange':
			result += ''.join('000')
			cnt += 1
			continue
		elif listd[cnt] == 'yellow':
			result += ''.join('0000')
			cnt += 1
			continue
		elif listd[cnt] == 'green':
			result += ''.join('00000')
			cnt += 1
			continue
		elif listd[cnt] == 'blue':
			result += ''.join('000000')
			cnt += 1
			continue
		elif listd[cnt] == 'violet':
			result += ''.join('0000000')
			cnt += 1
			continue
		elif listd[cnt] == 'grey':
			result += ''.join('00000000')
			cnt += 1
			continue
		elif listd[cnt] == 'white':
			result += ''.join('000000000')
			cnt += 1
			continue
print  ''.join(result)