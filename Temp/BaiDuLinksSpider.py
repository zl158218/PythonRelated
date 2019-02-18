# coding:utf-8
import re
import requests
import time

def dates(company):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    for page in range(0, 20, 10):
        try:
            url = 'https://www.baidu.com/s?ie=utf-8&cl=2&rtt=1&bsst=1&tn=news&word=' + company + '&x_bfe_rqs=03E80&x_bfe_tjscore=0.012060&tngroupname=organic_news&pn=' + str(page)
            res = requests.get(url, headers=headers)

            titles = []
            sources = []
            Release_time = []
            article_links = []

            if res.status_code == 200:
                title_re = '<h3 class="c-title">.*?>(.*?)</a>'
                title = re.findall(title_re, res.text, re.S) # 标题

                p_info = '<p class="c-author">(.*?)</p>'
                info = re.findall(p_info, res.text, re.S)  # 来源

                links_re = '<h3 class="c-title">.*?<a href=\"(.*?)\".*?data.*?>'
                links = re.findall(links_re, res.text, re.S)  # 链接

                for i in range(len(title)):
                    title[i] = title[i].strip()
                    title[i] = re.sub('<.*?>', '', title[i])
                    titles.append(title[i])
                # print(titles)

                for i in range(len(info)):
                    if len(info[i]) > 200:
                        # print(info[i], len(info[i]))
                        source =  re.findall('<img.*?/>(.*?)$', info[i], re.S)[0].split('&nbsp;&nbsp;')[0].strip()
                        time = re.findall('<img.*?/>(.*?)$', info[i], re.S)[0].split('&nbsp;&nbsp;')[1].strip()
                        sources.append(source)
                        Release_time.append(time)
                    else:
                        sources.append(info[i].split('&nbsp;&nbsp;')[0].strip())
                        Release_time.append(info[i].split('&nbsp;&nbsp;')[1].strip())

                for i in range(len(links)):
                    # print(links[i])
                    article_links.append(links[i])

                # 写入txt文件
                file1 = open(r'/media/aim/a61c08f4-b2ff-497d-bdf6-9efe8867b0a1/all_tmp/百度搜索结果链接爬虫/test.txt','a')
                file1.write(company + '消息监控completed！' + '\n' + '\n')
                for i in range(len(titles)):
                    file1.write(str(i) + ". " + titles[i] + "  " + "(" + sources[i] + "  " + Release_time[i] + ")" + '\n')
                    file1.write(article_links[i] + '\n')
                    file1.write('\n')
                file1.write('——————————————————————————————————————' + '\n' )
            print(company + '该公司爬取成功')
        except:
            print(company + '该公司爬取失败')


if __name__ == "__main__":
    # while True:
        companys = ['阿里巴巴', '腾讯', '京东', '华能信托', '百度集团']
        for company in companys:
            dates(company)
        time.sleep(20)
        print("All article Save to file successful...")










        # for i in range(len(titles)):
        #     print(str(i) + ". " + titles[i] + "  " + "(" + sources[i] + "  " + Release_time[i] + ")")
        #     print(article_links[i])
        #     print()