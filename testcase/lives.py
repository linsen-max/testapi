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

@pytest.mark.parametrize('data',read_yaml('LivesTestData.yaml'))
def test_livesList(data):
    headers = header
    r = requests.get(url+'api/noah/v2/lives?',params = data['params'], headers=headers)
    prepared = r.prepare()
    print(prepared)
    GeneraltTest(r)