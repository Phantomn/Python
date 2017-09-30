# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import Request
from mstechnet.items import MstechnetItem

reload(sys)
sys.setdefaultencoding('utf-8')

class MstechnetSpider(scrapy.Spider):
    name = "mstechnet"
    allowed_domains = ["technet.microsoft.com"]
    start_urls = ['https://technet.microsoft.com/ko-kr/security/advisories']

    def parse(self, response):
    	for href in response.xpath('//div[@id="sec_advisory"]//tbody/tr/td[3]/a/@href'):
    		url = response.urljoin(href.extract())
    		print "url : ", url
    		yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self,response):
    	for sel in response.xpath('//div[@id="sec_advisory"]'):
    		item = MstechnetItem()
    		item['title'] = sel.xpath('//tbody/tr/td[3]/a/text()').extract()
    		item['link'] = sel.xpath('//tbody/tr/td[3]/a/@href').extract()
    		print "title ",item['title']
    		print "link ", item['link']
    		yield item

    	'''desc = response.xpath(self.LINK_PATH)
    	if desc:
    		request = scrapy.Request(desc, callback=self.parse_desc_page)
    		yield request
    	#else:
    	#	self._save_data(item)

    def parse_desc_page(self,response):
    	for sel2 in response.xpath('//div[@id="body"]//div[@id="mainBody"]'):
    		item = MstechnetItem()
    		item['desc'] = sel2.xpath('/p[1]/text()') + sel2.xpath('/p[2]/text()') + sel2.xpath('/p[3]/text()')
    		print item['desc']
    		yield item


    def _save_data(self,data):
    	# TODO
    	pass'''