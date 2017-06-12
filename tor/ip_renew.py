from TorCtl import TorCtl
from urllib2 import *

user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)"
headers = {'User-Agent':user_agent}
oldIP = "0.0.0.0"
newIP = "0.0.0.0"
def request(url):
	def _set_urlproxy():
		proxy_support = ProxyHandler({"http" : "127.0.0.1:8118"})
		opener = build_opener(proxy_support)
		install_opener(opener)
	_set_urlproxy()
	request = Request(url, None, headers)
	return urlopen(request).read()

def renew_connection():
	conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="tmdvy123")
	conn.send_signal("NEWNYM")
	conn.close()

for i in range(0, 10):
    if oldIP == "0.0.0.0":
        renew_connection()
        oldIP = request("http://en.0day.today/")
    else:
		oldIP = request("http://en.0day.today/")
		renew_connection()
		newIP = request("http://en.0day.today/")
    while oldIP == newIP:
    	newIP = request("http://en.0day.today/")
    print request("http://en.0day.today/")