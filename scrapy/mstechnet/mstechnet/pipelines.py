# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem

class MstechnetPipeline(object):
	def __init__(self):
		self.file = codecs.open("mstechnet.json", "wb", encoding="utf-8")

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item


class DuplicatesPipeline(object):
	def __init__(self):
		self.titles_seen = set()
		self.links_seen = set()
		self.descs_seen = set()

		def process_item(self, item, spider):
			if item['title'] in self.titles_seen:
				raise DropItem("Duplicate item found : %s"%item)
			else:
				self.titles_seen.add(item['title'])
				return item
			if item['link'] in self.links_seen:
				raise DropItem("Duplicate item found : %s"%item)
			else:
				self.links_seen.add(item['link'])
				return item
			if item['desc'] in self.descs_seen:
				raise DropItem("Duplicate item found : %s"%item)
			else:
				self.descs_seen.add(item['desc'])
				return item