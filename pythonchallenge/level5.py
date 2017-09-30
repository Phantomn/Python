from urllib import *
from pickle import *

raw = load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
#print raw

for line in raw:
	print "".join([k * v for k, v in line])
