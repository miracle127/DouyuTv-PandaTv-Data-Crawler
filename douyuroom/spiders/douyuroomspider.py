import scrapy
from scrapy.http import Request
from ..items import DouyuroomItem
import json
import pandas as pd


class MySpider(scrapy.Spider):

    name = 'douyuroom'
    allowed_domains = ['douyucdn.cn']
    url = 'http://open.douyucdn.cn/api/RoomApi/room/'
    n = 0
    num = str(pd.datetime.now().strftime(format('%m%d%H')).replace('/', ' ')) + 'A'
    df = pd.read_json('/home/miracle/文档/douyu/' + num + 'douyudata.json')
    rmid = df['roomid']

    def start_requests(self):
        url = self.url+str(self.rmid[self.n])
        yield Request(url,self.parse)

    def parse(self, response):
        try:
            code = json.loads(response.text)['data']
            item = DouyuroomItem()
            item['owner_weight'] = str(code['owner_weight'])
            item['roomid'] = str(code['room_id'])
            item['fans_num'] = str(code['fans_num'])
            item['start_time'] = str(code['start_time'])
            item['selecttime'] = str(pd.datetime.now())
            yield item
            if self.n < len(self.rmid - 1):
                self.n += 1
                yield Request(self.url + str(self.rmid[self.n]), callback=self.parse)
            else:
                return
        except TypeError:
            print('type error')
            if self.n < len(self.rmid - 1):
                self.n += 1
                yield Request(self.url + str(self.rmid[self.n]), callback=self.parse)


