import requests
import json
URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.get(url=URL, data=json_data)
    else:
        r=requests.get(url=URL)
    data1=r.json()
    print(data1)

get_data()

