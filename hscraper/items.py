# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HscraperItem(scrapy.Item):
	name = scrapy.Field()
	branche = scrapy.Field()
	adresse = scrapy.Field()
	plz = scrapy.Field()
	ort = scrapy.Field()
	tel = scrapy.Field()
	fax = scrapy.Field()
	email = scrapy.Field()
	oeffnungszeiten = scrapy.Field()
	gmaps scrapy.Field()
	url = scrapy.Field()
