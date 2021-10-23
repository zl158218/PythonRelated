# -*- coding: utf-8 -*-
import os
import time
import datetime
from appium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}
desired_caps['noReset'] = True
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '7'     # 设备系统版本
desired_caps['deviceName'] = '127.0.0.1:62001'  # 设备名称  adb devices
desired_caps['appPackage'] = 'com.tencent.mm'   # 微信
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'  # 微信

# desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'  # 抖音
# desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'   # 抖音

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver, 300)

class OccupySeat:
    
    def __init__(self) -> None:
        while True:
            nows = datetime.datetime.now()
            if nows.hour == 6 and nows.minute == 59:
                self.run()
        
    def run(self):
        # 来选座
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.view.View[contains(@text, "来选座")]'))
        ).click()
        
        while True:
            nows = datetime.datetime.now()
            if nows.hour == 7 and nows.minute == 00:
                # 座位
                wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '// android.widget.TextView[@class="android.widget.TextView"][contains(@text, "座位")]'))
                ).click()
                break
        start_time = time.time()
        while True:
            TouchAction(driver).tap(x=249, y=1515).perform()
            time.sleep(0.1)
            TouchAction(driver).tap(x=800, y=1515).perform()
            if time.time() - start_time() > 5:
                break

    def give_like(self):
        """
        点赞
        """
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[1]'))).click()

        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, 'android:id/title'))).click()
        print("进入朋友圈")

        # 获取屏幕的size
        size = driver.get_window_size()
        # 获取屏幕宽度 width
        width = size['width']
        # 获取屏幕高度 height
        height = size['height']

        # 执行滑屏操作,向下（下拉）滑动
        x1 = width * 0.5
        y1 = height * 0.65
        y2 = height * 0.35
        time.sleep(1)
        # driver.swipe(x1, y1, x1, y2)
        # 增加滑动次数，滑动效果不明显，增加滑动次数
        n = 1
        while True:
            try:
                driver.swipe(x1, y1, x1, y2)
                time.sleep(2)
                content = wait.until(
                    EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/b_e")))

                txt = content.get_attribute('text')
                # print(txt)
                if len(txt) > 10:
                    try:
                        wait.until(
                            EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ik"))).click()
                    except Exception as exc:
                        continue

                    time.sleep(1.5)
                    try:
                        wait.until(
                            EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/i8"))).click()
                        n += 1
                        print(f"{n} 点赞： ", "\n", txt)
                        print("============================")
                    except Exception as exc:
                        content

                time.sleep(3)

            except Exception as exc:
                print("Error:", exc)
                continue


if __name__ == '__main__':
    OccupySeat()
