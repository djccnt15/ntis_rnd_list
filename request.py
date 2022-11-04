import json

import requests
from addict import Dict

with open('auth.json') as f:
    key = json.load(fp=f)

query = Dict(key)
query.collection = 'project'
query.searchFd = 'BI'
query.addQuery = 'PY=2020/MORE'
query.searchRnkn = 'DATE/DESC'
query.displayCnt = 1
query = query.to_dict()
print(query)

response = requests.post(
    url = 'https://www.ntis.go.kr/rndopen/openApi/public_project',
    data = query
)

print(response)
print(response.text)