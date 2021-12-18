"""
对于.ini类型的配置文件，使用configparser模块获取、修改内容
"""


import configparser

# 创建管理对象
config = configparser.ConfigParser()

# 读取.ini文件
file_ini = "IniFile.ini"
config.read(file_ini, "utf-8")

# 获取sectings、items、otptions、valua
config.sections()
config.items(section="")

config.options(section="")
config.get(section="", option="")

# 判断section、option是否存在
config.has_section("")
config.has_option(section="", option='')

# 移除section、option
config.remove_section(section="")
config.remove_option(section="", option="")

# 添加section、option、value
config.add_section(section="")
config.set(section="", option="", value="")

# 上面的方法并没有真正的修改ini文件内容，只有当执行conf.write()方法的时，才会修改文件里的内容
config.write(open(file_ini), 'a')

# 使用with open方法写入
with open(file_ini, 'a') as f:
    f.seek(2)   # 移动鼠标指针到末尾
    config.write(f)