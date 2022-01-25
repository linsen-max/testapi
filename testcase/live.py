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

http://static.www.t.ifboss.com/api/cmi-api/v1/live/new/topics?is_recommend=1&limit=20&page=1