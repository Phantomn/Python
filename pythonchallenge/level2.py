from urllib import *
import re

html = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
#print html
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
'''count = {}
for c in data:
	count[c] = count.get(c, 0) + 1

print count'''
print "".join(re.findall("[A-Za-z]", data))