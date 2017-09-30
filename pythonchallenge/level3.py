import urllib
import re

html = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
print "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]" ,data))