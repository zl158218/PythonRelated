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

__init__
    初始化方法，创建对象后，默认立刻被调用，可接收参数。
__new__
    1, 至少要有一个参数 cls
    2, 必须要有返回值
[详解1](https://zhuanlan.zhihu.com/p/58139772)
[详解2](https://mp.weixin.qq.com/s/SyC_LLQL8AU3i6wYNlOdNQ)
