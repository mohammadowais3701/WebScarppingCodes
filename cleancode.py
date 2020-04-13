from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import re
def cleanInput(inputs):
    inputs=re.sub('\n+'," ",inputs)
    inputs=re.sub('\[[0-9]*\]',"",inputs)
    inputs=re.sub(' +',' ',inputs)
    inputs=bytes(inputs,"UTF-8")
    inputs=inputs.decode("ascii","ignore")
   
    cleanInput=[]
    inputs=inputs.split(' ')
   
    for item in inputs:
        
        item=item.strip(string.punctuation)
        if len(item) > 1 or (item=='a' or item=='i'):
            cleanInput.append(item)
    return cleanInput        
def ngrams(inputs,n):
    inputs=cleanInput(inputs)
  
    output=[]
    for i in range(len(inputs)-n+1):
       
        output.append(inputs[i:i+n])
        
    return output
def getcontent(link):
    try:
        html=urlopen(link)
        bsObj=BeautifulSoup(html,features="html.parser")
    except HTTPError as e:
        return None
    try:
        content=bsObj.find("div",{"id":"mw-content-text"}).get_text()
    except AttributeError as e:
        return None
    return content
content=getcontent("http://en.wikipedia.org/wiki/Python_(programming_language)")


    


ngramss=ngrams(content,2)
print(ngramss)