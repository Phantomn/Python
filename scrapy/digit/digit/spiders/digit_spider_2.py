import scrapy
import sys
from digit.items import DigitItem
from scrapy.selector import HtmlXPathSelector


reload(sys)
sys.setdefaultencoding('utf-8')

class DigitSpider(scrapy.Spider):
	name = "digit_"
	allowed_domains = ["dt.co.kr"]
	start_urls = ['http://www.dt.co.kr/']


	def parse(self, response):
		for href in response.xpath('//nav[@id="nav"]/ul/li/a/@href'):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		hxs = HtmlXPathSelector(response)
		for name, title in zip(hxs.select('//nav[@id="nav"]/ul/li/a/text()').extract(),
								hxs.select('//nav[@id="nav"]/ul/li/a/@href').extract()):
			item = DigitItem()
			item['name'] = name.decode('utf-8')
			item['title'] = title.decode('utf-8')
			yield item