from bs4 import BeautifulSoup
from  selenium import webdriver
import time

driver=webdriver.PhantomJS(executable_path='C:\\PhantomJs\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
pageSource=driver.page_source
bsObj=BeautifulSoup(pageSource)
print(bsObj.find(id="content").get_text())