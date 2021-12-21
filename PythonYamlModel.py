"""关于yaml文件的格式及yaml模块的使用"""

import os
import yaml


def read_yaml(filedir):
    with open(filedir, 'r', encoding='utf-8') as f:
        date_yaml = yaml.full_load(f)
        return date_yaml


def write_yaml(obj, filedir):
    with open(filedir, 'w', encoding='utf-8') as f:
        yaml.dump(obj, f)


if __name__ == '__main__':
    date = read_yaml('YamlFile.yaml')
    print(date)
    dict_yaml = {'name': "muzi", 'email': 'honggang_li@icloud.com', 'phone': [15071110157, 1234567,987654]}
    path_dir = os.path.dirname(os.path.realpath('__file__'))
    path_yaml = os.path.join(path_dir, 'yaml_dump.yaml')
    write_yaml(dict_yaml, path_yaml)