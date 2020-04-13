import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
link=" http://py4e-data.dr-chuck.net/comments_417744.xml"
data=urllib.request.urlopen(link,context="ctx")
data=data.read()
tree=ET.fromstring(data)
results=tree.findall('comments/comment')
counts=0
for i in results:
    counts+=int(i.find("count").text)
print(counts)