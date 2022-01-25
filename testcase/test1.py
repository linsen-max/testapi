import random
import string
import requests
from headers import *
header = test_header().get_web()
url = test_header().url

def gen_cell_nums():
    # common_prefix = ['130', '131', '132', '133', '135', '136', '138', '139', '176', '180']
    common_prefix = ['162','165','167']
    result = []
    for i in range(100):
        result.append(random.sample(common_prefix, 1)[0] + ''.join(random.sample(string.digits, 8)))
    return result

result = gen_cell_nums()
assert len(set(gen_cell_nums())) == 100
print(result)

