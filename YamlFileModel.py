"""关于yaml文件的格式及yaml模块的使用"""

import yaml


def open_yaml_model(filedir):
    with open(filedir, encoding='utf-8') as f:
        date_yaml = yaml.full_load(f)
        return date_yaml


if __name__ == '__main__':
    date = open_yaml_model('PythonYaml.yaml')
    print(date)
    print(type(date))