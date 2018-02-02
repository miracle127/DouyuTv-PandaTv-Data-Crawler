# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
import pandas as pd


class JsonExporterPipeline:
    n = pd.datetime.now().strftime(('%d%H'))
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        now = pd.datetime.now().strftime(format('%m%d%H')).replace('/',' ')
        secend = int(pd.datetime.now().strftime(format('%M')))
        if secend<30:
            type = 'A'
        else:
            type = 'B'
        self.file = open('/home/miracle/文档/douyu/'+str(now)+type+'douyudata.json', 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # 开启倒数
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item