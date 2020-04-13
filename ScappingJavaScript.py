from  selenium import webdriver
import time
driver=webdriver.PhantomJS(executable_path='C:\\PhantomJs\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
print(driver.find_element_by_css_selector("#content").text)
print(driver.find_element_by_tag_name("div").text)
driver.close()