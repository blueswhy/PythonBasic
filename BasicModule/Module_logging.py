# 日志文件
# 默认情况下, python的logging模块将日志文件打印到标准输出中, 并且仅仅显示大于等于warning级别的日志,
# 日志文件等级为Critical>Error>Warning>Info>Debug. 默认日志格式: 日志级别-LoggerName--用户输出消息
import os
import logging
from logging import handlers
import time


# 1. 改变日志格式, 级别, 输出位置
#    日志格式规定查找python中的logging模块文件有对应说明

filename1 = '../demo' + os.sep + 'TestDoc' + os.sep + 'testlog1.log'
fileHandler = logging.FileHandler(filename1, 'a')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S %p',
    handlers=[fileHandler,],
    level=logging.ERROR
)

logging.error('Hello world!')

# 2. 日志切割
#    一般情况下, 程序日志只有在程序重启是才可以生成一个新的日志文件, 导致程序长时间运行之后, 会生成一个巨大的日志文件,
#    不方便后期问题查询或者磁盘清理, 因此一般使得日志按规定时间切割.
#    下面的实例中fileHdl按照时间间隔来切割日志, rotate基于文件大小对日志进行切分
filename2 = '../demo' + os.sep + 'TestDoc' + os.sep + 'testlog2.log'
streamHdl = logging.StreamHandler()
rotateHdl = handlers.RotatingFileHandler(filename1, maxBytes=64, backupCount=2)
fileHdl = handlers.TimedRotatingFileHandler(filename2, when='s', interval=5, encoding='utf-8')
logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S %p',
    handlers=[fileHdl, streamHdl, rotateHdl],
    level=logging.ERROR
)

for i in range(1000):
    time.sleep(0.01)
    logging.error(f'Keyboard Interrupt error:{i}')

