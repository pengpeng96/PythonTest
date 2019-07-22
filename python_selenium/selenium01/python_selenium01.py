
from selenium import webdriver

from time import sleep

# driver = webdriver.Chrome("D:\\selenium-webdriver\\chromedriver.exe")

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()

sleep(2)
title_str = driver.title
print(title_str)

# driver.quit()