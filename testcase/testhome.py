import xlrd
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath

testdata=xlrd.open_workbook(GetTestDataPath())


urlHost='static.www.t.ifboss.com'
apiHost='api.t.ifboss.com'
testurl='http://'+urlHost
testapi='http://'+apiHost

#Web一级导航栏设置
def get_htmlsetting():
    try:
        table = testdata.sheets()[1]
        for i in range(3,5):
            en_name=table.cell(i,0).value
            status=table.cell(i,1).value
            qiwang = table.cell(i,2).value
            hdata= {
                "en_name":str(en_name)
            }
            header = {
                'content-type': "application/json",
                'Host':urlHost
            }
            testcaseid="2-1"
            testname="testhome"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/api/cmi-api/v1/htmljssetting/en_name',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status_code")
    except Exception as e:
        print(e)

#get_htmlsetting()

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


get_homelives()