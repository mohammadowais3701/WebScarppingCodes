from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getfile(link):
    try:
        html=urlopen(link)
        bsobj=BeautifulSoup(html,features="html.parser")
    except HTTPError as e:
        print(str(e))
    try:
        imgloc=bsobj.find("a",{'id':'logo'}).find("img")["src"]
        urlretrieve(imgloc,"logo.png")
    except AttributeError as e:
        print(str(e))
getfile("http://www.pythonscraping.com")      
print("done")      

