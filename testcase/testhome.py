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

#testyaml=yaml.load(open(GetYamlDataPath()),Loader=yaml.FullLoader)
url = test_header().url
header = test_header().get_web()
#Web一级导航栏设置
#@pytest.mark.parametrize('data',read_yaml('HomeTestData.yaml'))
def test_get_htmlsetting():
    headers = header
    r = requests.get(url+'/api/cmi-api/v1/htmljssetting/en_name?en_name=web-website-setting', headers=headers)
    GeneraltTest(r)
    # re = json.loads(r.text)
    # assert r.status_code == 200
    # assert jsonpath.jsonpath(re, '$..status_code') == [0]

# get_htmlsetting()

#今日大事件
def test_get_breaking_news():
    headers = header
    r = requests.get(url + '/newapi/noah/v1/breaking-news', headers=headers)
    GeneraltTest(r)


#get_breaking_news()

#首页信息流
def test_get_timelines():
    headers = header
    r=requests.get(url+'/noah/v1/timelines',header=headers)
    GeneraltTest(r)

#get_timelines()

#首页金色热搜
def test_get_hot_search():
    headers = header
    r=requests.get(url+'/newapi/noah/v1/hot-search',headers=headers)
    GeneraltTest(r)

#get_hot_search()


def test_get_homelives():
    headers = header
    r=requests.get(url+'/newapi/noah/v1/flashes/simple',headers=headers)
    print(r.text)
    GeneraltTest(r)

#get_homelives()

#产业动向
def test_get_homeindustry():
    headers = header
    r=requests.get(url+'/newapi/noah/v1/timelines/other',headers=headers)
    print(r.text)
    GeneraltTest(r)
#get_homeindustry()
#近期活动
def get_activities():
    pass

#  /newapi/v1/hot/activities

#
# @pytest.mark.parametrize('mobile', ['13111111111', 15111111111, 18111111111, 0x2dfdc1c35, None])
# @pytest.mark.parametrize ('captcha',['123456',12345,'1234567',None])
# @pytest.mark.parametrize('area_code',[86,1,1472,None])
@pytest.mark.parametrize("data",read_yaml('HomeTestData.yaml'))
def test_post_login(data):
    headers = test_header().post_web(isneedlogin=data['isneedlogin'])
    print(headers)
    r=requests.post(url+'/api/ajax/user/login/captcha',json=json.loads(data['body']),headers=headers)
    re = json.loads(r.text)
    print(re)
    assert r.status_code == data['code']
    assert data['response'] in jsonpath.jsonpath(re,'$..*')
#
#
# @pytest.mark.parametrize('mobile',['13111111111','15111111111'])
# @pytest.mark.parametrize('captcha',['123456'])
# @pytest.mark.parametrize('area_code',[86])
# def test_pass_login(mobile,captcha,area_code):
#     payload = {'mobile': mobile, 'captcha': captcha, 'area_code': area_code}
#     r = requests.post(testurl + '/api/ajax/user/login/captcha', json=payload)
#     # r.encoding='utf-8'
#
#
# #if __name__ == '__main__':
# #    test_pass_login()
#
# mobile={'13111111111', 15111111111, 18111111111, 0x2dfdc1c35, None}
# captcha={'123456',12345,'1234567',None}
# area_code={86,1,1472,None}
# print(yaml.safe_dump_all([mobile, captcha,area_code], allow_unicode=True))
#
# with open(testyaml, 'w', encoding='utf-8') as f:
#     yaml.safe_dump_all([mobile, captcha,area_code], stream=f, allow_unicode=True)
