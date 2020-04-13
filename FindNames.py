from urllib.request import urlopen
from bs4 import BeautifulSoup
link="http://py4e-data.dr-chuck.net/known_by_Raegan.html"
for i in range(7):
    html=urlopen(link)
    bsObj=BeautifulSoup(html,features="html.parser")
    links=bsObj.find_all("a")
    link=links[17].get('href')
    print(links[17].text)

