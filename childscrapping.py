from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getLink(url):
    try:
        link=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(link.read(),features="html.parser")
        nameList=bsObj.find("table",{"id":"giftList"}).tr
    except AttributeError as e:
        return None
    return nameList
link=getLink("http://www.pythonscraping.com/pages/page3.html")    
for i in link.next_siblings:
    print(i)        
