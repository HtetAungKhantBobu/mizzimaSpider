# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TempItem(scrapy.Item):
    title=scrapy.Field()
    category=scrapy.Field()
    pubDate=scrapy.Field()
    author=scrapy.Field()
    body=scrapy.Field()
    img=scrapy.Field()
    ytlink=scrapy.Field()
    
