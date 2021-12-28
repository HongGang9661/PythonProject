class MyError(Exception):
    """自定义一个错误类型"""

    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return '错误原因为：' + self.parameter + '不是数字'


try:
    num = input('请输入一串数字：')
    if not num.isdigit():
        raise MyError(num)
    else:
        print('输入的数字为：' + str(num))
except MyError as my:
    print(my)
except SystemError:
    print('NOTHING')
except NameError:
    print('NameError' + N.name)
except Exception as e:
    print(e)
else:
    a = 1   # try模块不失败会执行
finally:
    b = 2   # 不管怎么样都会执行
