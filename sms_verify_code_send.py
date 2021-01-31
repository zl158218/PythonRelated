# coding:utf-8

import json
import time
import requests
from pprint import pprint
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Harass:
    def __init__(self):
        options = webdriver.ChromeOptions()
        
        # 无头模式
        # options.add_argument('--headless')
        options.add_argument('--window-size=1280,780')
        
        # 指定浏览器的位置
        # options.binary_location = '/opt/bin/headless-chromium'
        
        # 单进程运行
        # options.add_argument('--single-process')
        
        self.driver = webdriver.Chrome(options=options)
        
        # 隐式等待三秒
        self.driver.implicitly_wait(10)
        
    def main(self):
        # if self.yidong():
        self.safety()

    def yidong(self):
        self.driver.get("https://login.10086.cn/")
        time.sleep(1)
        self.driver.find_element_by_id('sms_login_1').click()
        time.sleep(1)
        self.driver.find_element_by_id('sms_name').send_keys('17810702820')
        self.driver.find_element_by_id('getSMSPwd1').click()
        time.sleep(10)
        return True

    def safety(self):
        self.driver.get("https://i.360.cn/login/?src=pcw_home&destUrl=https://www.360.cn/")
        time.sleep(1)
        try:
            self.driver.execute_script("""$("a[class='quc-tab-item-inner']").contents().trigger("click");""")
            
            # self.driver.find_element_by_css_selector("a[class='quc-tab-item-inner']").click()
            # time.sleep(1)
            # self.driver.find_element_by_name('mobile').send_keys('17810702820')
            # time.sleep(0.2)
            # self.driver.find_element_by_class_name('quc-link quc-get-token').click()
            
            time.sleep(1000)
        except Exception as exc:
            pprint(exc)

if __name__ == "__main__":
    Harass().main()