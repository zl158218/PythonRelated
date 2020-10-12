### 虎扑步行街爬取
  
  - https://github.com/zl158218/python/tree/master/HuPuBuXingJie_lol
  - 目标
    - 帖子名称
    - 帖子链接
    - 作者
    - 作者链接
    - 创建时间
    - 回复数
    - 浏览数
    - 最后回复时间
    - 最后回复用户
### scrapy
  - https://github.com/zl158218/python/tree/master/scrapy
  - 爬取回车桌面美女图


### 要点

```
# -*- coding: UTF-8 -*-


def func_one(**kwarges):
    """
    不定长度的键值对
    """
    print(kwarges)
    print(kwarges.get('name'))

def func_two(*arges):
    """
    非键值对可变参数的列表
    """
    print(arges)

if __name__ == "__main__":
    func_one(
        name="十叁",
        iq=130,
        eq=120,
    )
    # {'name': '十叁', 'iq': 130, 'eq': 120}
    # 十叁

    func_two(
        "十叁", 130, 120,
    )
    # ('十叁', 130, 120)

```

### 魔法方法
```
__init__
    初始化方法，创建对象后，默认立刻被调用，可接收参数。
__new__
    1, 至少要有一个参数 cls
    2, 必须要有返回值
```
- [详解1](https://zhuanlan.zhihu.com/p/58139772)
- [详解2](https://mp.weixin.qq.com/s/SyC_LLQL8AU3i6wYNlOdNQ)


### 语法相关
- #### 单引号，双引号，多引号区别
    > 同样的引号中间不能包含该引号，
    > 比如 单引号中间不能出现单引号，双引号中间不能出现双引号，
    > 
    > 多引号能同时包含单引号或双引号，否则 Python 无法确定字符串的结束位置。

### 爬虫相关

- #### 编码问题

  - #### 方案一
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
  - #### 方案二
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
  - #### 其他
    > res = res.text.encode(response.encoding).decode('utf-8')
