# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class DanawaItem(scrapy.Item):
        date = scrapy.Field()
	price = scrapy.Field()
