import requests
url="http://192.168.1.184:1212/stuinfo/"
r=requests.get(url=url)
data=r.json()
print(data)