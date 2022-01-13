import json

import jsonpath


def GeneraltTest(r):
    re = json.loads(r.text)
    assert r.status_code == 200
    assert jsonpath.jsonpath(re, '$..status_code') == [0]