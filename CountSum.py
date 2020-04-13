from urllib.request import urlopen
from bs4 import BeautifulSoup


html=urlopen('http://py4e-data.dr-chuck.net/comments_417742.html')
bsObj=BeautifulSoup(html,features="html.parser")
tags=bsObj.find_all('span',{"class":"comments"})
count=0
for i in tags:
    count+=int(i.text)
print(count)
