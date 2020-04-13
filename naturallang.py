from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import re
import operator

def isCommon(ngram):
   
    commonWords = ['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it',
    'i', 'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this',
    'they', 'is', 'an', 'at', 'but','we', 'his', 'from', 'that', 'not',
    'by', 'she', 'or', 'as', 'what', 'go', 'their','can', 'who', 'get',
    'if', 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will',
    'as', 'up', 'one', 'time', 'has', 'been', 'there', 'year', 'so',
    'think', 'when', 'which', 'them', 'some', 'me', 'people', 'take',
    'out', 'into', 'just', 'see', 'him', 'your', 'come', 'could', 'now',
    'than', 'like', 'other', 'how', 'then', 'its', 'our', 'two', 'more',
    'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because',
    'day', 'more', 'use', 'no', 'man', 'find', 'here', 'thing', 'give',
    'many', 'well']

      
           
       
    if (ngram[0].split(' '))[0] in commonWords:
        return True
    return False    
    
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
  
    output={}
    for i in range(len(inputs)-n+1):
        ngramtemp=" ".join(inputs[i:i+n])
        if ngramtemp not in output:
            output[ngramtemp]=0
        output[ngramtemp]+=1

        
    return output
def getcontent(link):
    try:
        html=str(urlopen(link).read(),'utf-8')
       
    except HTTPError as e:
        return None

    return html
content=getcontent("http://pythonscraping.com/files/inaugurationSpeech.txt")


    


ngramss=ngrams(content,2)
sortedNGrams = sorted(ngramss.items(), key = operator.itemgetter(1),
reverse=True)

for i in sortedNGrams:
    print(i)
    temp=isCommon(i)

    if temp==True:
      
        sortedNGrams.remove(i)
print(sortedNGrams)        

