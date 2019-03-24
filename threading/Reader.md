#### 多线程,多进程

- 并发和并行

  - 并发:  一个时间段内发生若干事件

  - 并行: 同一时刻发生若干事情

    > 例如: 任务是, "吃完一碗米饭和一碗青椒炒肉"，
    >
    > “并发”就是一个人吃，这个人吃一口菜然后吃一口饭，由于切换速度比较快，让你觉得他在“同时”吃菜和饭；
    >
    > “并行”就是两个人同时吃，一个人吃饭，一个人吃菜。

  - GIL 全局锁

    > GIL（Global Interpreter Lock） 即全局锁，它规定一个解释器在同一时间只能运行一个线程。
    >
    > Python的线程需要取得GIL才能运行，释放了GIL被其他线程拿去，其他线程才能开始运行，
    >
    > 所以Python的多线程不能做到并行（同时运行多个线程）

  - Threading

    ```
    run()	 用以表示线程活动的方法
    start()  启动线程
    join()   等待至线程终止.阻塞调用线程直至线程的joni()方法被调用为之
    isAlive()  返回线程是否是活动的  Ture,False
    getName()  返回线程名
    setName()  设置线程名
    ```

    

  - 多线程_对象

  ```
  # -*- coding:utf-8 -*-
  import threading
  import time
  import  requests
  def get_html():
      headers = {
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
      }
      html = requests.get('https://www.baidu.com',headers=headers)
      print(html.text[1:50])
      print()
  if __name__ == '__main__':
      get_html()
      threads = []
      try:
          for i in range(10):
              t = threading.Thread(target=get_html,args=())
              threads.append(t.start())
              print(time.strftime('%H:%M:%S'))
  
          for t in threads:
              t.join()
              print(time.strftime('%H:%M:%S'))
      except:
          print('Error..................')
  ```

  - 多线程_继承

  ```
  # -*- coding:utf-8 -*-
  import threading
  import time
  import  requests
  
  class MyThread(threading.Thread):
      def __init__(self,headers,num):
          threading.Thread.__init__(self)
          self.headers = headers
          self.num = num
      def run(self):
          get_html(self.headers,self.num)
  
  def get_html(headers,num):
      html = requests.get('https://www.baidu.com',headers=headers)
      print(html.text[1:50])
      print()
  
  if __name__ == '__main__':
      headers = {
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
      }
      thread_list = []
      for num in range(10):
          t = MyThread(headers,num)
          thread_list.append(t)
      for t in thread_list:
          t.start()
      for t in thread_list:
          t.join()
  ```

  

- 多进程

  ```
  import  multiprocessing
  import time
  
  def foo():
  	print(time.strftime("%H:%M:%S"))
  	print("一个进程")
  
  if __name__ == '__main__':
  	p = multiprocessing.Process(target=foo)
  	p.start()
  	
  ##############################
  #  	  开多个进程   
  ##############################
  import  multiprocessing
  import time
  
  def foo(i):
  	print("%d 号一个进程"%i )
  	print(time.strftime("%H:%M:%S"))
  	print()
  
  
  if __name__ == '__main__':
  	# p = multiprocessing.Process(target=foo)
  	# p.start()
  	for i in range(10):
  		p = multiprocessing.Process(target=foo,args=(i,))
  		p.start()
  	
  ```

  

