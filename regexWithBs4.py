from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
def getImages(url):
    try:
        link=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(link.read(),features="html.parser")
        imgs=bsObj.find_all("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})        
    except AttributeError as e:
        return None
    return imgs
imgs=getImages("http://www.pythonscraping.com/pages/page3.html")
for i in imgs:
    print(i["src"])            