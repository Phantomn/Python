# -*- coding: utf-8 -*-
import json
import codecs
from scrapy.exceptions import DropItem

class DigitPipeline(object):

	def __init__(self):
		self.file = codecs.open("digit.json", "wb", encoding="utf-8")

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

class DuplicatePipeline(object):

	def __init__(self):
		self.names_seen = set()
		self.titles_seen = set()

		def process_item(self, item, spider):
			if item['name'] in self.names_seen:
				raise DropItem("Duplicate item found : %s"%item)
			else:
				self.names_seen.add(item['name'])
				return item
			if item['title'] in self.titles_seen:
				raise DropItem("Duplicate item found : %s"%item)
			else:
				self.titles_seen.add(item['title'])
				return item
