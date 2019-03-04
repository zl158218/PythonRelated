# -*-  coding:utf-8 -*-
import requests
from urllib.parse import urlencode
import json
import pandas as pd
import numpy as np
import time
import datetime
import xlwt

def get_auction():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.106',
        'Proxy-Connection':'keep-alive',
        'Accept':'application/json'
    }
    data = {'username': 'username','password': 'password'}       # Form data 用户名，密码
    url = 'http://********************'  # 登录接口
    session = requests.Session()        # Session可以使用get，post等方法，Session对象在请求时允许你保留一定的参数和自动设置cookie     
    session.post(url,data=data)         # cookie保留在session 中
    for  page in range(1,20):  # 拍卖会记录第N页
        records_url =  'http://*******************' + str(page) + '&pageSize=10&filters=undefined&sortField=undefined&orderBy=undefined'   # 请求preview
        records = session.get(records_url)
        if records.status_code == 200:
            if records.json().get('data'):
                for item in records.json().get('data').get('list'):                    
                    details = item.get('auctionDeal')             
                    # auctionName = details.get('auctionName')    
                    horseName = details.get('horseName')          
                    priceCurrent = details.get('priceCurrent')   
                    chujia = item.get('bidPrice')                                    
                    buyer = item.get('buyer')            
                    bidding = buyer.get('name')                   
                    bidTime = item.get('bidTime')
            
                    timeearr = time.localtime(bidTime//1000)
                    BidTime = time.strftime("%Y-%m-%d %H:%M:%S",timeearr)

                    yield {
                        'horseName' : horseName,
                        'chujia' : chujia,
                        'bidding' : bidding,
                        'bidTime' : BidTime
                    }
                    # 'priceCurrent' : priceCurrent
        else:
            print("Url 无效...")    

if __name__ == "__main__":
    ex = xlwt.Workbook(encoding='utf-8')
    exsheet = ex.add_sheet("拍卖会记录",cell_overwrite_ok=True)
    data = get_auction()

    headline = ['马名', '竞拍方', '竞拍价格', '竞拍时间']
    hores = []
    ChuJia = []
    Bid_ding = []
    Bid_Time = []

    for i in data:
        records = list(i.values())
        hores.append(records[0])
        ChuJia.append(records[1])
        Bid_ding.append(records[2])
        Bid_Time.append(records[3])
    # 行写入，写入 表头 headline
    for head in range(0,len(headline)):
        exsheet.write(0,head,headline[head])
    # 列写入，0表示第一列，3表示第四列    
    for record in range(0,len(ChuJia)):
        exsheet.write(record+1,0,hores[record])
        exsheet.write(record+1,1,Bid_ding[record])
        exsheet.write(record+1,2,ChuJia[record])
        exsheet.write(record+1,3,Bid_Time[record])

    ex.save('拍卖会记录.xls')   # 文件保存到当前目录下，也可以自定义路径  ex.save(r'D:\example.xls')  
