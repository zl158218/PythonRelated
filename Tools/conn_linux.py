# -*- coding: utf-8 -*-
from loguru import logger
import paramiko
import time
import re

ip = "192.168.1.1"
username = "root"
port = 22
pw = "122122"


def conn_server(count: int = 0, max_count: int = 2):
    '''
    连接 Linux  服务器, 执行拨号命令并获取 IP
    :param count:  重试次数
    :param max_count:  最大重试次数
    :return:
    '''
    if count >= max_count:
        return False
    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=ip, port=port, username=username,
                    password=pw, timeout=15)
        
        # 执行 Shell 命令
        command = ['adsl-stop', 'adsl-start',
                   "pppoe-status | sed -n '/inet/'p"]
        stdin, stdout, stderr = ssh.exec_command(
            command=command[0], get_pty=True, timeout=60)
        stdin, stdout, stderr = ssh.exec_command(
            command=command[1], get_pty=True, timeout=60)
        # 重试次数
        nums = 0
        time.sleep(8)
        while True:
            # 监控执行命令结果
            stdin, stdout, stderr = ssh.exec_command(
                command=command[2], get_pty=True, timeout=60)
            proxy_ip_list = re.findall(
                'inet(.*?)peer', str(stdout.readlines()).replace(' ', ''), re.S)
            if proxy_ip_list:
                logger.info(proxy_ip_list)
                ssh.close()
                return proxy_ip_list[0]
            else:
                # 重试次数
                if nums < 4:
                    time.sleep(1)
                    nums += 1
                    continue
                else:
                    logger.info("拨号 IP 获取失败")
                    return False

    except Exception as ex:
        logger.info(f"拨号 IP 获取失败: {ex}")
        return False
