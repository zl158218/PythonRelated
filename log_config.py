# -*- coding: utf-8 -*-

from datetime import datetime
from github_api import main
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

"""
日志配置
@date: 2021-01-30
"""

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def set_logger():
    today = datetime.today().strftime('%Y-%m-%d')
    # 日志文件
    error_log = f"error_{today}.log"
    info_log = f"info_{today}.log"

    # 日志格式
    formatter = logging.Formatter('%(asctime)s Line: %(lineno)d %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    # 日志保存在文件
    file_log = TimedRotatingFileHandler(error_log, when='D', encoding="utf-8")
    file_log.setLevel(logging.ERROR)
    file_log.setFormatter(formatter)
    logger.addHandler(file_log)

    info_file = TimedRotatingFileHandler(info_log, when='D', encoding="utf-8")
    info_file.setLevel(logging.INFO)
    info_file.setFormatter(formatter)
    logger.addHandler(info_file)

    # 在终端查看日志
    console_log = logging.StreamHandler()
    console_log.setFormatter(formatter)
    logger.addHandler(console_log)


def main():
    logger.info("这是 INFO 测试日志")
    logger.debug("这是 DEBUG 测试日志")


if __name__ == '__main__':
    set_logger()
    main()
