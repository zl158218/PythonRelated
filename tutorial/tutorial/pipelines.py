# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymysql
import datetime
from tutorial import settings

class TutorialPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "insert into quotes (text,author,tags,submission_data) value(%s,%s,%s,%s)",(item['text'],item['author'],item['tags'],datetime.datetime.now()
            ))
            self.connect.commit()
            return item
        except Exception as error:
            logging.log(error)

    def close_spider(self,spider):
        self.connect.close();



'''
        # "insert into article (body, author, createDate) value(%s, %s, %s) on duplicate key update author=(author)",
        # (item['body'],
        #  item['author'],
        #  datetime.datetime.now()
        #  ))

def save_to_mysql(content):
    conn = MySQLdb.connect("localhost", "admin", "qweqwe", "hupu", charset='utf8')
    datas = conn.cursor()
    tuple_1 = (content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7])
    l0 = tuple_1[0]
    l1 = tuple_1[1]
    l2 = tuple_1[2]
    l3 = tuple_1[3]
    l4 = tuple_1[4]
    l5 = tuple_1[5]
    l6 = tuple_1[6]
    l7 = tuple_1[7]
    sql = "insert into hupu (titles,titles_urls,author,author_url,stick_time,reply,Last_reply_time,Finally_reply_author) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        datas.execute(sql,(l0,l1,l2,l3,l4,l5,l6,l7))
        conn.commit()
    except:
        conn.rollback()
    conn.close()

'''