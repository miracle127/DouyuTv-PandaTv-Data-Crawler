import scrapy
from scrapy.http import Request
import json
import pandas as pd
from ..items import PandatvItem
import time


class MySpider(scrapy.Spider):

    name = 'pandatv'
    url = 'http://route.showapi.com/1369-1?showapi_appid=46956&showapi_sign=358598ab582d4d9582cf55fbef125cc1&page='
    page = 1
    start_url = url + str(page)

    def start_requests(self):
        yield Request(self.start_url,callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)['showapi_res_body']
        try:
            data = data['data']
        except KeyError:
            print('neterror')
            yield Request(self.url+str(self.page),callback=self.parse)
        try:
            for i in data:
                item = PandatvItem()
                userinfo = i['userinfo']
                item['zhubo'] = userinfo['nickName']
                item['user_name'] = userinfo['userName']
                label = i['label']
                for j in label:
                    item['label1'] = j['cname']
                    item['label2'] = j['cname']
                item['roomid'] = str(i['id'])
                item['watcher'] = str(i['person_num'])
                item['title'] = str(i['name'])
                cate = i['classification']
                item['cate_name'] = str(cate['cname'])
                host = i['host_level_info']
                # item['n_lv'] = str(host['n_lv'])
                item['val'] = str(host['val'])
                item['vip'] = str(host['vip'])
                item['c_lv'] = str(host['c_lv'])
                item['c_lv_val'] = str(host['c_lv_val'])
                item['playday'] = str(host['plays_day'])
                item['bamboo_user'] = str(host['bamboo_user'])
                item['gift_cnt'] = str(host['gift_cnt'])
                item['n_lv_val'] = str(host['n_lv_val'])
                item['gift_user'] = str(host['gift_user'])
                item['selecttime'] = str(pd.datetime.now())
                yield item

        except TypeError:
            print('type error')
            pass
        if self.page>400:
            return
        else:
            time.sleep(0.5)
            self.page += 1
            yield Request(self.url + str(self.page), callback=self.parse)



