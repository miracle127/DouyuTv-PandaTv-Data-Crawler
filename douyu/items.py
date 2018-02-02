# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    zhubo = scrapy.Field()
    #主播名
    roomid = scrapy.Field()
    #房间号
    cate_name = scrapy.Field()
    #直播类别
    cate_id = scrapy.Field()
    #类别id
    title = scrapy.Field()
    #直播主题
    online = scrapy.Field()
    #当前观众数
    selecttime =scrapy.Field()
    #连续直播时间
