# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/i책 읽는 프로그래머tems.html

import scrapy
from scrapy.item import Item, Field

class MstechnetItem(scrapy.Item):
   title = scrapy.Field()
   link = scrapy.Field()
   desc = scrapy.Field()