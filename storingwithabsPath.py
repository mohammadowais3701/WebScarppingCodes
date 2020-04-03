import os
from urllib.request import urlretrieve,urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

downloadDirectory="downloaded"
baseURL="http://pythonscraping.com"

def getAbsoulteURL(baseURL,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("www."):
        url=source[4:]
        url="http://"+source[4:]
    elif source.startswith("http://"):
        url=source
    else:
        url=baseURL+"/"+source
    if baseURL not in url:
        return None
    return url
def getDownloadPath(baseURL,absoluteURL,downloadDirectory):

    path=absoluteURL.replace("www.","")
    path=path.replace(baseURL,"")
    path=downloadDirectory+path
    directory=os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    print("PATH..............."+path)   
    return path    
def getList(link):
    try:
        html=urlopen(link)
        bsObj=BeautifulSoup(html,features="html.parser")
    except HTTPError as e:
        print(str(e))
        return None
    try:
        downloadList=bsObj.findAll(src=True)
    except AttributeError as e:
        print(str(e))
        return None
    return downloadList    
lis=getList("http://www.pythonscraping.com")

if lis is not None:
    for download in lis:    
        fileURL=getAbsoulteURL(baseURL,download["src"])
        if fileURL is not None:
            print("file........"+fileURL)
urlretrieve(fileURL,getDownloadPath(baseURL,fileURL,downloadDirectory))
print('done')
                            