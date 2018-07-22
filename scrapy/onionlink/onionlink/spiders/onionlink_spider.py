# -*- coding: utf-8 -*-
import scrapy
import sys
from onionlink.items import OnionlinkItem
from scrapy.selector import HtmlXPathSelector
from scrapy import Request


class OnionlinkSpider(scrapy.Spider):
    name = "onionlink"
    allowed_domains = ["cyberi3qaiydq4we.onion"]
    start_urls = ['http://cyberi3qaiydq4we.onion/']

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)


    def parse(self, response):
    	item = OnionlinkItem()
