from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("https://count.problem.ctf.nw.fit.ac.jp/")
#src = browser.page_source

#print src.split("\n") 

while(True):

	body = browser.find_element_by_tag_name('body').text
	prob = body.split('\n')[0]

	username = browser.find_element_by_name("username")

	username.send_keys(str(eval(prob)))
        username.send_keys(Keys.ENTER)


	#browser.find_element_by_tag_name("form").click()
        time.sleep(2)
