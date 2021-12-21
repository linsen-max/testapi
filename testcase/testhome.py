import xlrd
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath

testdata=xlrd.open_workbook(GetTestDataPath())

testurl='http://static.www.t.ifboss.com'
testapi='api.t.ifboss.com'

def get_htmlsetting():
    try:
        table = testdata.sheets()[1]
        for i in range(3,5):
            status=table.cell(i,0).value
            qiwang = table.cell(i,1).value
            hdata=""
            header = {
                'content-type': "application/json",
                'Host':"static.www.t.ifboss.com"
            }
            testcaseid="2-1"
            testname="teshome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            status_code=""
            r=TestGetRequest(testurl+'/api/cmi-api/v1/htmljssetting/en_name?en_name=web-website-nav',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,status_code)
    except Exception as e:
        print(e)

get_htmlsetting()

#
def get_breaking_news():
    try:
        table = testdata.sheets()[1]
        for i in range(3,5):
            status=table.cell(i,0).value
            qiwang = table.cell(i,1).value
            hdata=""
            header = {
                'content-type': "application/json",
                'Host':"static.www.t.ifboss.com"
            }
            testcaseid="2-1"
            testname="teshome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            status_code=""
            r=TestGetRequest(testurl+'/newapi/noah/v1/breaking-news',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,status_code)
    except Exception as e:
        print(e)


def get_timelines():
    try:
        table = testdata.sheets()[1]
        for i in range(3,5):
            status=table.cell(i,0).value
            qiwang = table.cell(i,1).value
            hdata=""
            header = {
                'content-type': "application/json",
                'Host':"static.www.t.ifboss.com"
            }
            testcaseid="2-1"
            testname="teshome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            status_code=""
            r=TestGetRequest(testapi+'/noah/v1/timelines?catelogue_key=www&flag=up&information_id=4923&limit=20',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,status_code)
    except Exception as e:
        print(e)