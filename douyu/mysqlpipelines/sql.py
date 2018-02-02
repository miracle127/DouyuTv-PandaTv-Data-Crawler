import pymysql.cursors
from douyu import settings

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_DBNAME = settings.MYSQL_DBNAME
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT

config = {
          'host':MYSQL_HOST,
          'port':MYSQL_PORT,
          'user':MYSQL_USER,
          'password':MYSQL_PASSWORD,
          'db':MYSQL_DBNAME,
          'charset':'utf8',
          }
cnx = pymysql.connect(**config)
cur = cnx.cursor()

class mysql:

    @classmethod
    def insert_douyu(cls,zhubo,roomid,cate_name,cate_id,title,online,selecttime):
        sql = 'INSERT INTO douyu(zhubo,roomid,cate_name,cate_id,title,online,selecttime) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        param = {
            'zhubo':zhubo,
            'roomid':roomid,
            'cate_name':cate_name,
            'cate_id':cate_id,
            'title':title,
            'online':online,
            'selecttime':selecttime
        }
        cur.execute(sql,param)
        cnx.commit()
