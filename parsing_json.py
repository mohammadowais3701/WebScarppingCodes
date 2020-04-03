from urllib.request import urlopen
from urllib.error import HTTPError
import json

def getjson(ip):
    try:
        html=urlopen("http://freegeoip.app/json/"+ip).read().decode('utf-8')
        responseJson=json.loads(html)
    except HTTPError as e:
        print(str(e))
    return responseJson
dic=getjson("121.97.110.145")
print(dic)

