import pytest

from testcase.testhome import test_post_login
from testdata.getpath import GetTestConfig
import re
import configparser



class test_header:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(GetTestConfig('Environment.conf'))
        header = 'header'
        self.url = config[header]['testurl']
        self.api = config[header]['testapi']
        rule = r'(?<=//)\S+$'
        self.urlHost = re.search(rule, self.url, flags=0)
        self.apiHost = re.search(rule, self.api, flags=0)

    @pytest.mark.usefixtures(test_post_login)
    def post_web(self,isneedlogin,data_type = 'json'):
        headers = {
            'Host': self.urlHost,
            'Accept': 'application/json, text/plain, */*',
            'Conteny-Type': 'application/json'
        }
        if isneedlogin():
            headers.append()
        return headers


    def web_get_headers(self):
        pass
