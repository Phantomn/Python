import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://technet.microsoft.com/ko-kr/library/security/ms17-mar.aspx' + str(page)
		source_code = requests.get(url, allow_redirects=False)
		plain_text = source_code.text.encode('ascii', 'replace')
		soup = BeautifulSoup(plain_text, 'lxml')
		for link in soup.find_all("a"):
			href = link.get('href')
			title = link.string
			print href
			print title
			#print link
		page += 1


spider(1)