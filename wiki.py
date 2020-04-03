from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re 
pages=set()
def getLinks(url):
    global pages
    try:
        html=urlopen("http://en.wikipedia.org"+url)
    except HTTPError as e:
        print(e)
    try:
        bsObj=BeautifulSoup(html.read(),features="html.parser")
        links=bsObj.find_all("a",href=re.compile("^(/wiki/)"))
    except AttributeError as e:
        print(e)    
    finally:
        for i in links:
            if 'href' in i.attrs:
                if i.attrs['href'] not in pages:
                    newPage=i.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)
getLinks("")                    