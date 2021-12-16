"""
对于.ini类型的配置文件，使用configparser模块获取、修改内容
"""


import configparser

# 创建管理对象
config = configparser.ConfigParser()

# 读取.ini文件
file = "config.ini"
config.read(file, "utf-8")

# 获取sectings、items、otptions、valua
config.sections()
config.items(section="")

config.options(section="")
config.get(section="", option="")

# 判断section、option是否存在
config.has_section("")
config.has_option(section="")

# 移除section、option
config.remove_section(section="")
config.remove_option(section="", option="")

# 添加section、option、value
config.set(section="", option="", value="")