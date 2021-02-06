# -*- coding:utf-8 -*-
"""
# 简单实现了  微信消息自动发送
"""

import time
import psutil
import pywinauto
from pywinauto.keyboard import send_keys
from pywinauto.application import Application
import os
import win32api
import win32con
import win32clipboard as wcl  # 操控剪切板


class WeChat:

    def __init__(self):

        self.send_list = dict()
        self.PID = int()

        # 默认消息
        # self.message = time.strftime("%Y-%m-%d %H:%M:%S") + " " + eval(config.get('message'))
        # self.message = eval(config.get('message'))
        self.message = input("输入发送消息内容：")
        self.contact = str(input("请输入发送人的微信号或者备注："))
        self.send_num = input("输入发送消息次数：")
        self.send_speed = input("发送间隔时间 |单位秒：")
        self.handle()
        self.default_contact()

    def handle(self):
        """
        获取微信 PID 及连接
        :return:
        """
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                if 'WeChat.exe' == pinfo['name']:
                    self.PID = pinfo['pid']
                    break
        else:
            print("微信未登陆，请先登陆微信")
            return False

        # 得到微信路径
        wechat_path = psutil.Process(self.PID).exe()

        # 连接微信
        Application().start(wechat_path)
        self.app = Application(backend='uia').connect(process=self.PID)
        self.win = self.app[u'微信']

    def default_contact(self):
        """
        选择默认联系人
        :return:
        """
        # 点击搜索
        addresslist = self.win.child_window(title="搜索", control_type="Edit")
        cords = addresslist.rectangle()
        pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))
        # pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))

        # 查询默认联系人
        self.win.Edit.type_keys((self.contact), with_spaces=True)
        time.sleep(0.5)
        # 回车
        send_keys('{ENTER}')

    def control(self):
        """
        发送文本消息
        """

        wcl.OpenClipboard(None)  # 打开剪贴板并
        wcl.EmptyClipboard()     # 清空剪贴板
        wcl.SetClipboardData(win32con.CF_UNICODETEXT, self.message)  # 向剪贴板中写入信息
        wcl.CloseClipboard()     # 关闭剪贴板
        n = int(self.send_num)
        m = 0
        while True:
            m += 1
            if m > n:
                return True

            win32api.keybd_event(17, 0, 0, 0)  # ctrl
            win32api.keybd_event(86, 0, 0, 0)  # V
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0);
            win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(13, 0, 0, 0)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0);
            time.sleep(float(self.send_speed))

        #     # 输入消息并回车发送
        #     self.win.Edit.type_keys((self.message), with_spaces=True).type_keys('{ENTER}')
        #     logger.info(f"发送成功-------- {self.message}  ---------------")

        # 查看控件树
        # print(win.print_control_identifiers())
        # addresslist = self.win.child_window(title=u"会话", control_type="List")
        # for i in range(2):
        #     send_keys('+{TAB}')
        #
        # time.sleep(0.3)
        # for i in range(10):
        #     send_keys('{DOWN}')
        #
        # time.sleep(0.1)
        # # 鼠标右击
        # send_keys('{VK_APPS}')

        # # 定位聊天记录
        # addresslist = self.win.child_window(title=self.message, control_type="Edit")
        # # addresslist = win.child_window(title="微信消息控件定位1", control_type="Edit")
        # cords = addresslist.rectangle()
        # pywinauto.mouse.click(button='right', coords=(cords.left, cords.top))

        # # 定位聊天记录为图片
        # addresslist = win.child_window(title="[图片]", control_type="ListItem")
        # cords = addresslist.rectangle()
        # pywinauto.mouse.click(button='right', coords=(cords.left, cords.top))

        # # 定位转发并点击
        # mess_text = self.win.child_window(title=u"转发", control_type="Text")
        # cords = mess_text.rectangle()
        # pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))
        #
        # # 选择群进行发送
        # self.select_contacts()
        #
        # # win.Edit.type_keys((self.group_chat), with_spaces=True).type_keys('{ENTER}')
        # # 发送
        # send = self.win.child_window(title=u"发送", control_type="Button")
        # cords = send.rectangle()
        # pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))

        # send = win.child_window(title=u"发送(S)", control_type="Button")
        # win = pywinauto.mouse.click(button='left', coords=(cords.left + 400, cords.top + 100))
        # addresslist = win.window(class_name="文件传输助手")
        # addresslist = win.child_
        # addresslist = win.child_window(title="大家好，我是微信机器人，", control_type="Text")
        # cords = addresslist.rectangle()
        # print(addresslist.print_ctrl_ids())
        # print(win.print_cl_ids())
        # static_wxh = win.child_window(title=self.send_list.get('massage'), control_type="Text")
        # Pane46 = static_wxh.parent().parent()
        # for item in Pane46.children():
        #     item.draw_outline()
        #     lines = item.children()
        #     # key = lines[0].window_text()
        #     # value = lines[1].window_text()
        #     # page[key] = value
        # 选择消息， 进行群发
        # addresslist = win.child_window(title="文件传输助手", control_type="Text")
        # print(dir(addresslist))
        # x = app[u'微信'][self.send_list.get('massage')]
        # x.Properties.TabControlSharing.select(self.send_list.get('massage'))
        # 消息群发
        # addresslist = win.child_window(title=self.send_list.get('massage'), control_type="Text")
        # print(addresslist.print_ctrl_ids())
        # cords = addresslist.rectangle()
        # button指定左击还是右击， coords指定鼠标点击的位置
        # addresslist = win.child_window(title=self.send_list.get('massage'), control_type="Text")
        # cords = addresslist.rectangle()

    def send_file(self):
        """
        发送文件消息
        :return:
        """
        # 选择文件
        addresslist = self.win.child_window(title="发送文件", control_type="Button")
        cords = addresslist.rectangle()
        pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))
        time.sleep(1)
        # child_window(title="地址: C:\Users\zl158\Pictures\8K", auto_id="1001", control_type="ToolBar")
        addresslist = self.win.child_window(control_type="ToolBar", auto_id="1001")
        cords = addresslist.rectangle()
        pywinauto.mouse.click(button='left', coords=(cords.left + 11, cords.top + 13))

        for folder, dirs, files in os.walk(os.path.join(os.path.join(os.getcwd(), 'message_file'))):
            self.win.Edit.type_keys(folder, with_spaces=True)
            time.sleep(1)
            send_keys('{ENTER}')
            time.sleep(0.5)
            send_keys('{ENTER}')
            time.sleep(0.5)
            send_keys('^a^c')
            time.sleep(0.5)
            send_keys('{ENTER}')
            send_keys('{ENTER}')
            break

        for i in range(2):
            time.sleep(1)
            send_keys('+{TAB}')

        time.sleep(0.3)
        for i in range(10):
            send_keys('{DOWN}')

        time.sleep(1)
        # 鼠标右击
        send_keys('{VK_APPS}')
        # 或者shift + F10
        # send_keys('+{F10}')
        mess_text = self.win.child_window(title=u"转发", control_type="Text")
        cords = mess_text.rectangle()
        pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))
        self.select_contacts()
        send = self.win.child_window(title=u"发送", control_type="Button")
        cords = send.rectangle()
        pywinauto.mouse.click(button='left', coords=(cords.left, cords.top))

        # image_location = self.win.child_window(title="[图片]", control_type="Text")
        # cords = image_location.rectangle()
        # pywinauto.mouse.click(button='right', coords=(cords.left, cords.top))

    def select_contacts(self):
        """
        选择多个联系人群发
        :return:
        """

        config = configparser.ConfigParser()
        # 文件路径
        logFile = "config.cfg"
        config.read(logFile, encoding="utf-8")
        config = config.defaults()

        for i in eval(config.get('group_chat')):
            self.win.Edit.type_keys((i), with_spaces=True).type_keys('{ENTER}')
            time.sleep(0.5)
            send_keys('^a{DELETE}')

        for i in eval(config.get('friend')):
            self.win.Edit.type_keys((i), with_spaces=True).type_keys('{ENTER}')
            time.sleep(0.5)
            send_keys('^a{DELETE}')


if __name__ == '__main__':
    WeChat().control()