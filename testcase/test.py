

import base64
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    s={
    "api": 'https://api.jinse.cn/',
    "tj-api": "https://tj.jinse.cn/",
    "h5-domian": "https://h5.jinse.com/",
    "m-domain": "https://m.jinse.com/"
}
    print(type(s))
    s_s = str(s)
    print(type(s_s))
    b_s = bytes((s_s),encoding='utf-8')
    print(type(b_s))
    a = base64.b64encode(b_s)
    return {"data":a}

home()
# testyaml=yaml.load(open(GetYamlDataPath()),Loader=yaml.FullLoader)
#
#
# mobile={'13111111111', 15111111111, 18111111111, 0x2dfdc1c35, None}
# captcha={'123456',12345,'1234567',None}
# area_code={86,1,1472,None}
# print(yaml.safe_dump_all([mobile, captcha,area_code], allow_unicode=True))
#
# with open(GetYamlDataPath(),'a', encoding='utf-8') as f:
#     yaml.safe_dump_all([mobile, captcha,area_code], stream=f, allow_unicode=True)
#

# def open1():
#     fo = open(GetYamlDataPath(),'r',encoding='utf-8')
#     res = yaml.load_all(fo,Loader=yaml.FullLoader)
#     for i in res:
#         print(i)
#
# open1()

