# -*-  coding:utf-8  -*-
import  pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import pymysql
from  matplotlib.font_manager import *
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

def rank():
    conn = pymysql.connect(
        host = '192.168.178.128',
        user = 'root',
        passwd = 'qweqweqwe',
        db = 'centos'
    )
    cur = conn.cursor()
    # sql = 'select horse_name,COUNT(horse_name) as 次数 from race_record,race where race.id=race_record.race_id and distance="1000" and pos != "退赛" GROUP BY horse_name ORDER BY 次数 DESC ;'
    # 查询出赛超过三次的马匹
    # sql = 'select * from   (select horse_name,COUNT(horse_name) as n from race_record,race where race.id=race_record.race_id and distance="1000" and pos != "退赛" GROUP BY horse_name ORDER BY n DESC ) c  where n > 3 ;'
    # sql = 'select * from   (select horse_name,COUNT(horse_name) as n from race_record,race where race.id=race_record.race_id and distance="1000" and pos != "退赛" GROUP BY horse_name ) c  where n > 5 ;'

    sql = " select  horse.name as 马名, sum(match_yl_regular_log.score) as 积分  from match_yl_regular_log,horse,race  where race_id=race.id  and  race.distance between '1000' and '1200'   and horse_id=horse.id  and race.start_datetime > '2018-04-19 14:40:00' group by horse.name order by 积分 desc limit 10"

    cur.execute(sql)   #     # 执行SQL语句，查询操作
    results = cur.fetchall()        # 获取所有记录列表

    horse_name = []
    numbers = []
    for i in results:
        horse_name.append(i[0])
        numbers.append(i[1])

    bar_width=0.3
    plt.bar(horse_name,numbers,bar_width,color='b')    #sales_BJ直方图
    plt.show()


if __name__ == '__main__':
    rank()
