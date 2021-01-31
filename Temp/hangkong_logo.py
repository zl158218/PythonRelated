import requests
from lxml import etree
import os


def gete_url():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }
    url = 'http://data.carnoc.com/corp/airline/'
    urls = requests.get(url).text
    # print(urls)
    html = etree.HTML(urls)
    message = html.xpath('//div[@class="corp_sub_list"]//a')

    list = []
    for i in message:
        title = i.xpath('./text()')[0]
        page = i.xpath('./@href')[0]

        list2 = [title, page]
        list.append(list2)
    return list


def gete_logo(urls):
    # print(title)
    logo_html = requests.get(urls)
    logos = etree.HTML(logo_html.text)
    logo_url = logos.xpath('//div[@class="logo z"]//img/@src')[0]
    return logo_url


def save_logo(title, logo_url):

    # 创建文件夹操作
    path = '/home/aim/图片/'
    if not os.path.exists(path):
        os.makedirs(path)

    content = requests.get(logo_url).content
    print("开始下载logo%s" % title)
    with open(path+title, 'wb') as f:
        f.write(content)
        f.close()
    print("图片下载完成")


def main():
    message = gete_url()
    for i in message:
        logo_url = gete_logo(i[1])
        save_logo(i[0], logo_url)

    for url in urls:
        # print(url['title'])
        logo = gete_logo(url['url'], url['title'])
        save_logo(logo)


if __name__ == "__main__":
    try:
        main()
    except:
        print("跳过")
