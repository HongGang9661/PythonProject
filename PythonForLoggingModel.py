""""
记录对logging模块的使用，掌握日志记录
Logger 暴露了应用程序代码能直接使用的接口。
Handler将（记录器产生的）日志记录发送至合适的目的地。
Filter提供了更好的粒度控制，它可以决定输出哪些日志记录。　　　
Formatter 指明了最终输出中日志记录的布局

CSDN：https://blog.csdn.net/weixin_30338743/article/details/99422394?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-1.highlightwordscore&spm=1001.2101.3001.4242.2
"""

import logging
import time


class LoggerModel:
    def __init__(self):
        # 创建日志记录器
        self.logger = logging.getLogger('logger')

    def get_log(self):
        # 设置日志器级别
        self.logger.setLevel(logging.DEBUG)
        # 定义Handler输出格式
        format_log = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

        # 如果没有处理器时，创建日志处理器，否则不创建
        if not self.logger.handlers:
            # 创建日志处理器Handler，用于写入日志文件
            logfile = '{}.txt'.format(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
            fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
            fh.setLevel(logging.INFO)
            # 设置Handler输出格式
            fh.setFormatter(format_log)
            # 将Handler添加到日志记录器
            self.logger.addHandler(fh)

            # 创建一个Handler用于控制台输出日志
            sh = logging.StreamHandler()
            sh.setLevel(logging.INFO)
            sh.setFormatter(format_log)
            self.logger.addHandler(sh)

        return self.logger


if __name__ == '__main__':
    log = LoggerModel().get_log()
    log.debug('这是一个debug的日志！')
    log.info('这是一个info的日志！')
    log.warning('这是一个warning的日志！')
    log.error('这是一个error的日志！')
    log.critical('这是一个critical的日志！')