from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

html=urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html,features="html.parser")
rows=bsObj.find_all("table",{"class":"wikitable"})[0].find_all("tr")  
with open('wikitable.csv','wt',encoding="utf-8") as csvFile:
    writer=csv.writer(csvFile)
    try:
        for row in rows:
            csvRow=[]
            for cell in row.find_all(['td','th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    finally:
        csvFile.close()