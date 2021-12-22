""""记录对logging模块的使用，掌握日志纪律"""

import logging

# 创建日志记录器
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建日志处理器Handler，用于写入日志文件
logfile = 'log.txt'
log_handler_file = logging.FileHandler(logfile, mode='a', encoding='utf-8')
log_handler_file.setLevel(logging.INFO)

# 定义Handler输出格式
format_log = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
log_handler_file.setFormatter(format_log)

# 将Handler添加到日志记录器
logger.addHandler(log_handler_file)

# 创建一个Handler用于控制台输出日志
log_handler_stream = logging.StreamHandler()
log_handler_stream.setLevel(logging.INFO)
log_handler_stream.setFormatter(format_log)
logger.addHandler(log_handler_stream)

logger.debug('这是一个debug的日志！')
logger.info('这是一个info的日志！')
logger.warning('这是一个warning的日志！')
logger.error('这是一个error的日志！')
logger.critical('这是一个critical的日志！')
