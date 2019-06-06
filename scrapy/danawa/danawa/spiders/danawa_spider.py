# -*- coding: utf-8 -*-
import scrapy
import sys
from danawa.items import DanawaItem
from scrapy.selector import HtmlXPathSelector
from scrapy import Request


class DanawaSpider(scrapy.Spider):
    name = 'danawa'
    allowed_domains = ['danawa.com']
    start_urls = ['http://prod.danawa.com/info/?pcode=5834197&keyword=SSD&cate=112760']

    def start_requests(self):
    	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    	for url in self.start_urls:
    		yield Request(url, headers=headers)
    def parse(self, response):
        item = DanawaItem()
        for sel in response.xpath('//div[@id="lowPriceCash"]'):
        	item['price'] = sel.xpath('//span[2]/a/em/text()').extract()
        	yield item
