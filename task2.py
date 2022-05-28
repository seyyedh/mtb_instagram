import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

username = ""
password = ""

driver = webdriver.Firefox()
url = 'https://www.instagram.com/p/B9U5rz5AsI8/'
url_login = "https://www.instagram.com/accounts/login/"

driver.get(url_login)
time.sleep(7)

element_user = driver.find_element_by_name("username")
element_pass = driver.find_element_by_name("password")
element_user.send_keys(username)
element_pass.send_keys(password)
element_user.submit()

time.sleep(10)

driver.get(url)

comment_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
comment_box.send_keys("This is a comment")

submit_key = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()

