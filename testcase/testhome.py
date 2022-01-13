import json
import jsonpath
import xlrd
import re
from headers import *
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath
import pytest
import requests
from YamlHandle import read_yaml

#testyaml=yaml.load(open(GetYamlDataPath()),Loader=yaml.FullLoader)
testdata=xlrd.open_workbook(GetTestDataPath())
testurl='http://static.www.t.ifboss.com'
testapi='http://api.t.ifboss.com'

rule = r'(?<=//)\S+$'
urlHost=re.search(rule, testurl, flags=0)
apiHost=re.search(rule, testapi, flags=0)
#Web一级导航栏设置
#@pytest.mark.parametrize('data',read_yaml('HomeTestData.yaml'))
def test_get_htmlsetting():
    headers = test_header().get_web()
    r = requests.get(testurl+'/api/cmi-api/v1/htmljssetting/en_name?en_name=web-website-setting',headers = headers)
    re = json.loads(r.text)
    assert r.status_code == 200
    assert jsonpath.jsonpath(re, '$..status_code') == [0]

# get_htmlsetting()

#今日大事件
def get_breaking_news():
    try:
        table = testdata.sheets()[1]
        for i in range(17,18):
            status=table.cell(i,0).value
            qiwang = table.cell(i,1).value
            hdata=""
            header = {
                'content-type': "application/json",
                'Host':urlHost
            }
            testcaseid="2-2"
            testname="testhome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/newapi/noah/v1/breaking-news',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status_code")
    except Exception as e:
        print(e)

#get_breaking_news()

#首页信息流
def get_timelines():
    try:
        table = testdata.sheets()[1]
        for i in range(32,33):
            catelogue_key=table.cell(i,0).value
            flag=table.cell(i,1).value
            information_id=table.cell(i,2).value
            limit=table.cell(i,3).value
            status=table.cell(i,4).value
            qiwang = table.cell(i,5).value
            hdata={
                "catelogue_key":str(catelogue_key),
                "flag":str(flag),
                "information_id":int(information_id),
                "limit":int(limit)
            }
            header = {
                'content-type': "application/json",
                'Host':apiHost
            }
            testcaseid="2-3"
            testname="testhome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testapi+'/noah/v1/timelines',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status_code")
    except Exception as e:
        print(e)

#get_timelines()

#首页金色热搜
def get_hot_search():
    try:
        table = testdata.sheets()[1]
        for i in range(47,48):
            status = table.cell(i,0).value
            qiwang = table.cell(i,1).value
            hdata=""
            header = {
                'content-type': "application/json",
                'Host':urlHost
            }
            testcaseid="2-4"
            testname="testhome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/newapi/noah/v1/hot-search',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status_code")
    except Exception as e:
        print(e)

#get_hot_search()


def get_homelives():
    try:
        table = testdata.sheets()[1]
        for i in range(63,65):
            limit= table.cell(i,0).value

            flag= table.cell(i,1).value
            category= table.cell(i,2).value
            status = table.cell(i,3).value
            qiwang = table.cell(i,4).value
            hdata={
                "limit":limit,
                "flag":flag,
                "category":int(category)
            }
            header = {
                'content-type': "application/json",
                'Host':urlHost
            }
            testcaseid="2-5"
            testname="testhome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/newapi/noah/v1/flashes/simple',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status_code")
    except Exception as e:
        print(e)


#get_homelives()

#产业动向
def get_homeindustry():
    try:
        table = testdata.sheets()[1]
        for i in range(77,80):
            limit=table.cell(i,0).value
            flag= table.cell(i,1).value
            information_id=table.cell(i,2).value
            catelogue_key = table.cell(i, 3).value
            status = table.cell(i,4).value
            qiwang = table.cell(i,5).value
            hdata={
                "limit":limit,
                "flag":flag,
                "information_id":information_id,
                "catelogue_key":catelogue_key
            }
            header = header.web_get_headers()
            #     {
            #     'content-type': "application/json",
            #     'Host':urlHost
            # }
            testcaseid="2-6"
            testname="testhome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/newapi/noah/v1/timelines/other',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status_code")
    except Exception as e:
        print(e)

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
    r=requests.post(test_header().url+'/api/ajax/user/login/captcha',json=json.loads(data['body']),headers=headers)
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
