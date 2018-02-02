import scrapy
from scrapy.http import Request
from ..items import DouyuItem
import json
import pandas as pd


class MySpider(scrapy.Spider):

    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    url = 'http://open.douyucdn.cn/api/RoomApi/live?limit=100&offset='
    offset = 0
    start_url = url+str(offset)


    def start_requests(self):
        url = self.start_url
        yield Request(url,self.parse)

    def parse(self, response):
        next_flag = False
        room_code = json.loads(response.text)['data']
        for i in room_code:
            next_flag = True
            item = DouyuItem()
            item['zhubo'] = str(i['nickname'])
            item['roomid'] = str(i['room_id'])
            item['cate_name'] = str(i['game_name'])
            item['cate_id'] = str(i['cate_id'])
            item['title'] = str(i['room_name'])
            item['online'] = str(i['online'])
            item['selecttime'] = str(pd.datetime.now())
            yield item
        if next_flag:
            self.offset+=100
            yield Request(self.url+str(self.offset))


