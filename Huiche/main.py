# from scrapy import cmdline
from scrapy.cmdline import execute
import sys
import os
#调试,文件路径
# print(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","Desk"])
# cmdline.execute("scrapy crawl jobbole".split())