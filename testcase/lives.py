import json
import jsonpath
import xlrd
import re
from headers import *
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testcase.GetGeneraltTest import GeneraltTest
from testdata.getpath import GetTestDataPath
import pytest
import requests
from YamlHandle import read_yaml

url = test_header().url

header = test_header().get_web()
#快讯列表
@pytest.mark.parametrize('data',read_yaml('LivesTestData.yaml'))
def test_livesList(data):
    headers = header
    r = requests.get(url+'api/noah/v2/lives?',params = data['params'], headers=headers)
    # prepared = r.prepare()
    # print(prepared)
    GeneraltTest(r)

#金色热搜
def test_hotsearch():
    headers = header
    r = requests.get(url+'/newapi/noah/v1/hot-search',headers=headers)
    GeneraltTest(r)


#今日大事件详情页
def test_coin_circle():
    headers = header
    r = requests.get(url+'/coin_circle',headers = headers)
    GeneraltTest(r)