### 方案一
```
import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC'
res = requests.get(url,headers=headers)
res.encoding = res.apparent_encoding
print(res.text)
```
### 方案二
```
# 如果网站返回的页面较大，会影响爬虫速度
# coding:utf-8
import chardet
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC'
res = requests.get(url,headers=headers)
res.encoding =chardet.detect(res.content)['encoding']
print(res.text)
print(res.encoding)
```

> html_text = response.text.encode(response.encoding).decode('utf-8')
