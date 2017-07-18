# -*- coding: utf-8 -*-
import scrapy
import sys
from zeroday.items import ZerodayItem
from scrapy.selector import Selector
from scrapy import Request
import re

reload(sys)
sys.setdefaultencoding('utf-8')


class ZerodaySpider(scrapy.Spider):
    name = "zeroday"
    allowed_domains = ["mvfjfugdwgc5uwho.onion"]
    start_urls = ['http://mvfjfugdwgc5uwho.onion/rss']

    def start_requests(self):
    	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    	for url in self.start_urls:
    		yield Request(url, headers=headers)

    def parse(self, response):
    	hxs = Selector(response)
    	for title, link, pubDate in zip(hxs.xpath('//item/title/text()').extract(),
    									hxs.xpath('//item/link/text()').extract(),
    									hxs.xpath('//item/pubDate/text()').extract()):
    		item = ZerodayItem()
    		item['title'] = title
    		item['link'] = link
    		item['pubDate'] = pubDate
    		yield item