import yaml


class YamlHandle(object):

    def __init__(self, conf_file):
        self.conf_file = conf_file

    def load(self) -> dict:
        """
        读取yaml文件，获取全部数据
        :return: dict
        """
        with open(file=self.conf_file, encoding='utf8') as f:
            data = yaml.load(f, yaml.FullLoader)
        return data

    def get_data(self, node) -> list:
        """
        获取节点数据
        :param node: 节点名称
        :return: dict&str
        """
        return self.load()[node]