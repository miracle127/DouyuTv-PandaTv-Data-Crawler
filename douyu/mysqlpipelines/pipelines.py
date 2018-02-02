from douyu.mysqlpipelines.sql import mysql
from douyu.items import DouyuItem


class DouyuPipeline(object):

    def process_item(self,item,spider):
        if isinstance(item,DouyuItem):
            zhubo = item['zhubo']
            roomid = item['roomid']
            cate_name = item['cate_name']
            cate_id = item['cate_id']
            title = item['title']
            online = item['online']
            selecttime = item['selecttime']
            mysql.insert_douyu(zhubo,roomid,cate_name,cate_id,title,online,selecttime)
            print('开始储存数据')