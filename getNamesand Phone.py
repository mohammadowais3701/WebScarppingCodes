from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getNamesandNumber(link):
    try:
      url=urlopen(link)
    except HTTPError as e:
        print(str(e))
        return
    try:
        bsObj=BeautifulSoup(url.read(),features='html.parser')
        nameList=bsObj.find_all('span',{'class':'None'})
    except AttributeError as e:
        print(str(e))
        return
lis=getNamesandNumber('https://www.truepeoplesearch.com/results?name=Aaron&agerange=45-74')
print(lis)

