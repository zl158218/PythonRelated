# coding:utf-8
'''
目标 2019年3月10 日到 4月1日，所有航班的信息动态
出发地，目的地，日期
各个仓位对应的价格
起飞时间，降落时间
# url = "https://www.ly.com/Flight/FlightBookAjax.aspx?Type=GetAllCity&_dAjax=callback&callback=tc1818278580"  # 城市接口
'''
import requests
import json
import re


def citys_list(headers):
    '''城市对应的offPort,arrPort的code，出发地，目的地'''

    city_url = "https://www.ly.com/Flight/FlightBookAjax.aspx?Type=GetAllCity&_dAjax=callback&callback=tc1818278580"
    city_json = requests.get(city_url, headers=headers)
    if city_json.status_code == 200:
        city_data = json.loads(re.findall(
            'tc1818278580\((.*?)\)', str(city_json.text))[0])['citys']

        straing_point = str(input("请输入起飞城市（出发地）： "))
        destination = str(input("请输入降落城市（目的地）： "))
        date_s = str(input("请输入出发时间（例如：2019-03-10）： "))

        if straing_point in city_data and destination in city_data:

            citys_dict = {}    # 定义一个字典，添加出发地，目的地，出发日期
            straing_codes = city_data.get(straing_point).get('code')
            destination_code = city_data.get(destination).get('code')

            citys_dict['straing'] = str(straing_codes)
            citys_dict['destination'] = str(destination_code)
            citys_dict['date'] = date_s
            return citys_dict
        else:
            print("城市输入有误，请重新输入。")
            return citys_list(headers)


def ticket(straing_code, end_code, date):
    """获取机票所有信息"""
    url = "https://www.ly.com/Flight/FlightQueryInterFace.aspx?Type=QRYFLIGHTINFOFORTQ&sort=0&errinner=&TcA=0&FilterList=&CabinCode=all&FlightNum=&CompanyCode=all&domain=&plat=&key=B9706D48D6D54250A616559CF3620B26&IsRevisionAfter=fznew&querytype=0&fquerykey=59da9afc-0e00-46ec-b36a-b8e2a46758f8&cztype=&IfVip=0&FqdLoginKey=1548646230989951&firstday=2019-03-05&isNew=1&offPort=" + \
        straing_code + "&arrPort=" + end_code + "&date=" + \
        date + "&queryParagraph=1&issoldiepolice=0"
    # url = "https://www.ly.com/Flight/FlightQueryInterFace.aspx?Type=QRYFLIGHTINFOFORTQ&sort=0&errinner=&TcA=0&FilterList=&CabinCode=all&FlightNum=&CompanyCode=all&domain=&plat=&key=B9706D48D6D54250A616559CF3620B26&IsRevisionAfter=fznew&querytype=0&fquerykey=59da9afc-0e00-46ec-b36a-b8e2a46758f8&cztype=&IfVip=0&FqdLoginKey=1548646230989951&firstday=2019-03-05&isNew=1&offPort=PEK&arrPort=SHA&date=2019-03-10&queryParagraph=1&issoldiepolice=0"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': 'www.ly.com',
        'Connection': 'keep-alive'
    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        # print(req.text)
        return req.text


def datas(data):
    test2 = data.split("result\":\"")[1].split("|")

    # 定义两个列表  flight 航班， all_price 全部舱位的价格
    flight = []
    all_price = []
    for i0 in range(0, len(test2), 2):
        flight.append(test2[i0])

    for i1 in range(1, len(test2), 2):
        all_price.append(test2[i1])

    airlines_list = []
    ticket_data_list = []
    take_off_time = []
    for f1 in range(len(flight)-1):
        airlines = flight[f1].split(
            ',')[1] + "--" + flight[f1].split(',')[2]  # 航空公司
        ticket_data = flight[f1].split(
            ',')[19]                               # 机票日期

        # 起飞及降落时间
        take_off_airplane = flight[f1].split(
            ',')[3] + " ---> " + flight[f1].split(',')[5]

        airlines_list.append(airlines)
        ticket_data_list.append(ticket_data)
        take_off_time.append(take_off_airplane)

        # print()
        # print(airlines)
        # print(ticket_data)
        # print(take_off_airplane)

    for a0 in range(len(all_price)):
        try:
            # print(all_price[a0].split(","))
            print()
            preferential = all_price[a0].split(
                ",")[22][-14:-6].replace('^', "") + "--￥" + all_price[a0].split(",")[0]   # 同程特惠
            economy_class = all_price[a0].split(
                ",")[66][-14:-6].replace('^', "") + "--￥" + all_price[a0].split(",")[55]  # 经济舱
            # 高端经济舱                                                                                                     #
            premium_economy = all_price[a0].split(
                ",")[110][-14:-6].replace('^', "") + "--￥" + all_price[a0].split(",")[110][-4:]
            # 全价经济舱                                                                                                     #
            full_fare_economy = all_price[a0].split(
                ",")[132][-14:-6].replace('^', "") + "--￥" + all_price[a0].split(",")[99]
            return_package = all_price[a0].split(",")[154][-14:-6].replace('^', "") + "--￥" + str(int(
                all_price[a0].split(",")[132][-4:].replace("*", "")) - int(all_price[a0].split(",")[147]))  # 往返优惠

            print("===========================")
            print("航空公司：", airlines_list[a0])
            print("起飞时间：", ticket_data_list[a0])
            print("起飞及降落时间：", take_off_time[a0])
            print("同程特惠：", preferential)
            print("经济舱：", economy_class)
            print("高端经济舱：", premium_economy)
            print("全价经济舱：", full_fare_economy)
            print("往返优惠：", return_package)
            print()
        except:
            print("查询失败")


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': 'www.ly.com',
        'Connection': 'keep-alive'
    }
    city = citys_list(headers)
    req_data = ticket(city['straing'], city['destination'], city['date'])
    datas(req_data)


if __name__ == '__main__':
    main()
