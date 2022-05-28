import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

username_login = ""
password_login = ""

driver = webdriver.Firefox()
url = 'https://www.instagram.com/p/B9U5rz5AsI8/'
driver.get(url)
time.sleep(7)
element_user = driver.find_element_by_name("username")
element_pass = driver.find_element_by_name("password")
element_user.send_keys(username_login)
element_pass.send_keys(password_login)
element_user.submit()
time.sleep(10)

cookie = driver.get_cookies()
print(cookie)
with open("cookie.txt", "w") as file:
    file.write(str(cookie))

