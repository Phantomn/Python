import scrapy

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from digit.items import DigitItem


print "============================================="
print "[*]Start Digital Times Crawling...."
print "============================================="



class DigitSpider(scrapy.Spider):
	name = "digit"
	allowed_domains = ["dt.co.kr"]
	start_urls = ['http://www.dt.co.kr/']
	def parse(self, response):
		print "[*]Parsing Digital Times pagelink..."

		for href in response.xpath('//nav[@id="nav"]/ul/li/a/@href'):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		for sel in response.xpath('//nav[@id="nav"]/ul/li'):
			item = DigitItem()
			item['name'] = sel.xpath('a/text()').extract()
			item['title'] = sel.xpath('a/@href').extract()
			yield item

