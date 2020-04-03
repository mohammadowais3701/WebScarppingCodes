from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getSpan(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html.read())
        nameList=bsObj.find_all("span",{"class":"green"})
    except AttributeError as att:
        return None
    return nameList
nameList=getSpan("http://www.pythonscraping.com/pages/warandpeace.html")   
for i in nameList:
    print(i.get_text())
        
