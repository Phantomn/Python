# -*- coding: utf-8 -*-
import scrapy
import sys
from seebug.items import SeebugItem
from scrapy.selector import Selector
from scrapy import Request
import re

reload(sys)
sys.setdefaultencoding('utf-8')

class SeebugSpider(scrapy.Spider):
    name = "seebug"
    allowed_domains = ["www.seebug.org"]
    start_urls = ['https://www.seebug.org/rss/new/']


    def parse(self, response):
        hxs = Selector(response)
    	for title, link, desc, category, pubDate in zip(hxs.xpath('//item/title/text()').extract(),
    									hxs.xpath('//item/link/text()').extract(),
    									hxs.xpath('//item/description/text()').extract(),
    									hxs.xpath('//item/category/text()').extract(),
    									hxs.xpath('//item/updated_date/text()').extract()):
    		item = SeebugItem()
    		item['title'] = title
    		item['link'] = link
    		item['desc'] = desc
    		item['category'] = category
    		item['pubDate'] = pubDate
    		yield item
