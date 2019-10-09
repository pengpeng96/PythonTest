# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 拿到driver
driver = webdriver.Chrome()

# 跳转网页
driver.get("https://xdclass.net")

print(driver.title)
# 睡眠时间3秒
sleep(3)

# 登录框
login_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.login > span:nth-child(2)")
ActionChains(driver).click(login_ele).perform()

sleep(2)
# 查找输入框，输入账号密码，输入框需要提前清理
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("13602694157")
driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("peng12345678")
# 点击登录
driver.find_element_by_css_selector(".btn").click()

# # 判断是否登录成功
# # 将鼠标移动到头像，判断弹窗字符
sleep(5)
# use_info_ele = driver.find_element_by_css_selector(".avatar_img")
use_info_ele = driver.find_element_by_css_selector('#app > div > div.header > div > div.r_userinfo.f_r > div.avatar.f_r > img')
# 触发hover事件
ActionChains(driver).move_to_element(use_info_ele).perform()
#
# 获取用户名的元素
user_name_ele = driver.find_element_by_css_selector('#app > div > div.header > div > div.userbox.f_r > div > div.user > p')


print('====测试结果===')
print(user_name_ele.text)
#
name = user_name_ele.text
#
if name == 'pengpeng':
    print('登录成功')
else:
    print('登录失败')

