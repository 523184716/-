#!/usr/bin/env python
#coding:utf-8

import  logging
import sys
import  os

# 获取logger实例，如果参数为空则返回root logger
# logger = logging.getLogger("AppName")
#
# # 指定logger输出格式
# formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
#
# # 文件日志
# file_handler = logging.FileHandler("test")
# file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
#
# # 控制台日志
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.formatter = formatter  # 也可以直接给formatter赋值
#
# # 为logger添加的日志处理器
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
#
# # 指定日志的最低输出级别，默认为WARN级别
# logger.setLevel(logging.INFO)
#
# # 移除一些日志处理器
# logger.removeHandler(file_handler)


class Logger():
    def __init__(self):
        logging.basicConfig(filename = "test.log",level=logging.DEBUG,
                            format='%(asctime)s %(filename)s %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
        # logging.getLogger(__file__)
        # print __file__

    def debug(self,message):
        logging.debug(message)
# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create file handler
logname = os.path.dirname(os.path.abspath(__file__))
log_path = logname+os.sep+"log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

# create formatter
# fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(process)d %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)



if __name__ == "__main__":
    # logger = Logger()
    # logger.debug("user")
    # logger = logging.getLogger("test")
    # logger.info("aaa")
     print logger.warning("dddd")
    # filename = "test.log",
    # logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d %H%M%S")
    # logging.info("message")
