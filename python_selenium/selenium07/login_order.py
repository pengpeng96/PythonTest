# -*- coding :utf-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("测试结束")
        pass
        # 单个测试用例结束

    def test_login_order(self):
        u"登录测试用例"
        driver = self.driver

        # 登录框
        login_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.login > span:nth-child(2)")
        ActionChains(driver).click(login_ele).perform()

        sleep(2)
        # 查找输入框、输入账号、输入框要提前清理里面的数据
        driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").clear()
        driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").send_keys("13602694157")
        # 查找密码输入框，输入密码
        driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").clear()

        driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").clear()
        driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").send_keys("peng12345678")

        # 拿到登录按钮
        login_btn_ele = driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.login_btn > button")
        # 触发点击事件，登录
        login_btn_ele.click()
        # 判断登录是否成功，逻辑——》 鼠标移到上面，判断弹窗字符
        # 获取鼠标上移的元素
        user_info_ele = driver.find_element_by_css_selector("#app")

        sleep(5)
        # hover触发
        ActionChains(driver).move_to_element(user_info_ele).perform()

        sleep(5)
        # # 获取用户名称元素
        # use_name_ele = driver.find_element_by_class_name("username")
        #
        # print("====测试结果====")
        # print(use_name_ele.text)

        # name = use_name_ele.text
        # # self.assertEqual(name ,u"pengpeng96",msg= "登录失败")
        # video_ele = driver.find_element_by_css_selector("div.hotcourses:nth-child(3)>div:nth-child(2)")
        # video_ele.click()
        # sleep(2)
        #
        # buy_btn_ele = driver.find_element_by_css_selector(".learn_btn > a:nth-child(1)")
        #
        # buy_btn_ele.click()
        # print("进入下单界面")

if __name__ == '__main__':
        unittest.main()