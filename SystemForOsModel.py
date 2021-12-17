import os

os.access(path="", mode=os.F_OK)
"""
os.access(path, mode);
参数
path -- 要用来检测是否有访问权限的路径。
mode -- 参数包含：
os.F_OK: 作为access()的mode参数，测试path是否存在。
os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
os.W_OK: 包含在access()的mode参数中 ， 测试path是否可写。
os.X_OK: 包含在access()的mode参数中 ，测试path是否可执行。
"""

#  用于改变当前工作目录到指定的路径。
os.chdir(path="")

# 查看当前工作路径
os.getcwd()

# 更改文件权限
os.chmod(path="", mode="")

# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.listdir(path="")

# 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
os.rmdir(path="")

# 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
os.remove(path="")

# 重命名文件或目录，从src到dst
os.rename(src="", dst="")

# 打开、读写操作文件
os.open(path="", flags="")
os.write()

# 创建多级目录：
os.makedirs(name="")

# 创建单个目录：
os.mkdir(path="")

# 指示你正在使用的平台,对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
os.name

# 用于创建一个指定文件名
os.mknod(path="")

# 目录结构
os.path.dirname("")  # 去掉文件名返回目录
os.path.basename("")  # 去掉目录返回文件名
os.path.dirname(__file__)  # __file__表示当前文件的路径
os.path.realpath(path="")  # 获取当前执行脚本的绝对路径，可使用内置函数__file__获取当前文件的路径，可以和os.path.dirname()组合使用
os.path.join("path1", "path2")  # 把目录和文件名合成一个路径
os.path.split("path")  # 把路径分割成 dirname 和 basename，返回一个元组
