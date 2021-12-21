"""关于yaml文件的格式及yaml模块的使用"""

import yaml


def read_yaml(filedir):
    with open(filedir, encoding='utf-8') as f:
        date_yaml = yaml.full_load(f)
        yaml.dump()
        return date_yaml


if __name__ == '__main__':
    date = read_yaml('')
    print(date)
    print(type(date))