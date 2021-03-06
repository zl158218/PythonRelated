import re
import requests


def problems(company):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    url = 'https://news.sogou.com/news?query=%B0%A2%C0%EF%B0%CD%B0%CD&mode=1&w=01029901&sut=4093&sst0=1550469559927&lkt=3%2C1550469555738%2C1550469559823'
    url = 'https://news.sogou.com/news?query=' + company + \
        '&mode=1&w=01029901&sut=4093&sst0=1550469559927&lkt=3%2C1550469555738%2C1550469559823'
    res = requests.get(url, headers=headers).text

    re_title = '<h3 class="vrTitle">.*?<a href=".*?" id="uigs_.*?" target="_blank">(.*?)</a>.*?</h3>'
    title_list = re.findall(re_title, res, re.S)

    re_data = '<p class="news-from">(.*?)&nbsp;(.*?)<!--.*?-->'
    data_list = re.findall(re_data, res, re.S)

    re_url = '<h3 class="vrTitle">\n<a href="(.*?)" id="u.*?" target="_blank">.*?</a>'
    url_list = re.findall(re_url, res, re.S)

    for i in range(len(title_list)):
        title_list[i] = re.sub('<.*?>', '', title_list[i])
        title_list[i] = re.sub('&.*?;', '', title_list[i])

        print()
        print(str(i) + '. ' +
              title_list[i] + "(" + data_list[i][0] + data_list[i][1] + ")")
        print(url_list[i])


companys = ['华能信托', '阿里巴巴', '万科集团', '百度', '腾讯', '京东']

for company in companys:
    try:
        problems(company)
        print(company, "爬取成功------------------------------")
    except Exception as exc:
        print("Fails", e)
