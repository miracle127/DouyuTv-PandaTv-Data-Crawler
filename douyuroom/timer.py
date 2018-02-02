import time
import os
os.system('cd /home/miracle/PycharmProjects/untitled2/douyuroom')
i = 1
while True:
    print('开始第%d次斗鱼TV房间信息爬取'%i)
    start = int(time.time())
    os.system('scrapy crawl douyuroom')
    print('第%d次斗鱼TV房间信息爬取结束'%i)
    end = int(time.time())
    i+=1
    time.sleep(3600-(end-start))


