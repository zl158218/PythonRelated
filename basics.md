# 基础系列

## Python 内存管理机制
- 引用计数
- 垃圾回收
    - 引用计数
    
        `Python 对象被引用时，引用计数加 1，当其减少一个变量引用时则计数减 1，当引用计数等于 0 时，对象被删除`
        
        `如果出现循环引用得话，引用计数机制就不再起有效作用`
    - 标记清除
    
        `如果两个对象的引用计数都为 1，但是仅仅存在他们之间的循环引用，那么这两个对象都是需要被回收的，他们的引用计数虽然表现为非 0，但实际上有效的引用计数为 0，所以先将循环引用摘掉，就会得出这两个对象的有效计数`
    - 分代回收
    
        `当需要回收的内存块越多时，垃圾检测带来的额外操作就越多，而垃圾回收带来的额外操作就越少；`
        
        `反之，当需回收的内存块越少时，垃圾检测就将比垃圾回收带来更少的额外操作。`
- 内存池


    [详情1](https://www.zhihu.com/question/30747394/answer/1001368660)

    [详情2](https://juejin.cn/post/6844903811375431694)

    [详情3](https://juejin.cn/post/6844903954325700621)

    [详情4](https://segmentfault.com/a/1190000016078708)

    [详情csdn](https://www.cnblogs.com/shengulong/p/10143856.html
    )

    [官网文档](https://docs.python.org/zh-cn/3.7/c-api/memory.html)


## 单例模式
> [视频地址](https://www.bilibili.com/video/BV1nt411s7qH?from=search&seid=15865521890966644423)
```python
# -*- coding: UTF-8 -*-
from typing import Any


class SingletonPatten:
    
    __obj = None
    __init_flag = True
    
    
    def __new__(cls, *args, **kwargs) -> Any:
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        
        return cls.__obj
    
    def __init__(self, name):
        if SingletonPatten.__init_flag:
            print('init...')
            self.name = name
        SingletonPatten.__init_flag = False
        

a = SingletonPatten("aa")
b = SingletonPatten("bb")

print(a)
print(b)

c = SingletonPatten("cc")
print(c)
```

## 闭包
> 内部函数对外部函数作用域的引用

```python
def func_one():
    name = 'Tom'
    def func_two(friend):
        print(f"{name} & {friend}")
    return func_two

func_one()("Jerry")
# Tom & Jerry

#---其他---
globals() # 以dict的方式存储所有全局变量
locals()  # 以dict的方式存储所有局部变量
```


- [参考](https://mp.weixin.qq.com/s/IySEKZoqIj1K2rM5_Hx8pw)