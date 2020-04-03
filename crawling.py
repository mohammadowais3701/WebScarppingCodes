from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
pages=set()
def getURLS(url):
    try:
        link=urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj=BeautifulSoup(link.read(),features='html.parser')
        links=bsObj.find('div',{'id':'bodyContent'}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        return None

    return links
links=getURLS("http://en.wikipedia.org/wiki/Kevin_Bacon")
for i in links:
    if 'href' in i.attrs:
         print(i.attrs['href'])   