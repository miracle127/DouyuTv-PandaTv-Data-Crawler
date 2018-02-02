import time
import os
os.system('cd /home/miracle/PycharmProjects/untitled2/panda')
i = 1
while True:
    print('开始熊猫TV第%d爬取'%i)
    start = int(time.time())
    os.system('scrapy crawl pandatv')
    print('第%d次熊猫TV爬取结束'%i)
    end = int(time.time())
    i+=1
    time.sleep(1800-(end-start))