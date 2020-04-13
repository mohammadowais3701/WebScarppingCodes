import json
from urllib.request import urlopen

link="http://py4e-data.dr-chuck.net/comments_417745.json"
data=urlopen(link,context="ctx")
info=json.loads(data.read())
counts=0
for i in info['comments']:
    counts+=i['count']
print(counts)