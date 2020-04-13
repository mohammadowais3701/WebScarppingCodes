import re

with open('actualdata.txt','r') as file:
    data=file.read()

    count=re.findall('[0-9]+',data)
    sum=0
    for i in range(len(count)):
        sum=sum+int(count[i])
    print(sum)    
    file.close()