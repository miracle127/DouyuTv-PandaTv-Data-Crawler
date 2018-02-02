# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuroomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    owner_weight = scrapy.Field()
    fans_num = scrapy.Field()
    start_time = scrapy.Field()
    roomid = scrapy.Field()
    selecttime = scrapy.Field()
