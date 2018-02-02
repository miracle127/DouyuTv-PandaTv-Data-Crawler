# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PandatvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhubo = scrapy.Field()
    #主播名
    user_name = scrapy.Field()
    #房间号
    label1 = scrapy.Field()
    #直播类别
    label2 = scrapy.Field()
    #类别id
    roomid = scrapy.Field()
    #当前观众数
    watcher =scrapy.Field()
    #连续直播时间
    title = scrapy.Field()
    #主播名
    cate_name = scrapy.Field()
    #房间号
    n_lv = scrapy.Field()
    #直播类别
    val = scrapy.Field()
    #类别id
    vip = scrapy.Field()
    #直播主题
    c_lv = scrapy.Field()
    #当前观众数
    c_lv_val =scrapy.Field()
    #连续直播时间
    playday = scrapy.Field()
    #直播类别
    bamboo_user = scrapy.Field()
    #类别id
    gift_cnt = scrapy.Field()
    #直播主题
    n_lv_val = scrapy.Field()
    #当前观众数
    gift_user =scrapy.Field()

    selecttime = scrapy.Field()