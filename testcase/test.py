import json
import jsonpath
import xlrd
import re
import yaml
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath
from testdata.getpath import GetYamlDataPath
import pytest
import requests
testurl='http://static.www.t.ifboss.com'

testyaml=yaml.load(open(GetYamlDataPath()),Loader=yaml.FullLoader)
testdata=xlrd.open_workbook(GetTestDataPath())
print(testyaml)


@pytest.mark.parametrize('mobile',['13111111111','15111111111'])
@pytest.mark.parametrize('captcha',['123456'])
@pytest.mark.parametrize('area_code',[86])
def test_pass_login(mobile,captcha,area_code):
    payload = {'mobile': mobile, 'captcha': captcha, 'area_code': area_code}
    r = requests.post(testurl + '/api/ajax/user/login/captcha', json=payload)
    # r.encoding='utf-8'


# if __name__ == '__main__':


