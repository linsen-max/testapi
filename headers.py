import json

import pytest
import jsonpath
import requests
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
        self.urlHost = (re.search(rule, self.url, flags=0).group())
        self.apiHost = (re.search(rule, self.api, flags=0).group())
        self.headers = {}
        self.token = ''

    def url(self):
        return self.url
    def api(self):
        return self.api

    def headerdirt(self):
        headerdirt = {
            'Host': self.urlHost,
            'Accept': 'application/json, text/plain, */*',
            'Conteny-Type': 'application/json'
        }
        return headerdirt

    def get_token(self):
        if 'token' in self.headers:
            pass
        else:
            payload = {
                "mobile": "13111111111",
                "captcha": "123456",
                "area_code": 86
            }
            r = requests.post(url=self.url+'/api/ajax/user/login/captcha',json=payload,headers=self.headerdirt())
            req = json.loads(r.text)
            token = jsonpath.jsonpath(req, '$..token')
            self.token = str(token)
            self.headers.update({'token': self.token})

    def post_web(self,isneedlogin = 'false'):
        if isneedlogin:
            self.get_token()
        else:
            if 'token' in self.headers:
                del self.headers['token']
        self.headers.update(self.headerdirt())
        return self.headers

    def get_web(self):
        self.headers.update(self.headerdirt())
        return self.headers
