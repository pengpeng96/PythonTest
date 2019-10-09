'''
第八章、自动化测试selenium和unittest整合项目实战

    1、小D课堂官网项目需求说明
        简介：讲解小D课堂官方自动化测试需求场景，和项目基础框架搭建

        1、自动化测试里面的测试用例设计的一些方法
            解耦、可以独立运行、需要灵活切换
            设计思路：脚本功能分析（分步骤）和模块化分层（拆分为多模块）

        project
             login_order.py    # 登录下单测试用例
             category.py      # 菜单分类测试用例

             all_test.py      # 主入口




    2、自动化测试实战之下单自动化测试
        简介：使用unittest + selenium 下单测试用例编写
        1、使用原先的资料   第5章第3集      第6章第4集



    3、分类列表整合unittest自动化测试
        简介：使用unittest + selenium 菜单弹窗测试用例编写

        1、使用资料  第5章第2集
        
'''

#下单自动化测试

# import unittest
# import HTMLTestRunner
# from time import sleep
# from selenium import  webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# class XdclassTestCase(unittest.TestCase):
#     def setUp(self):
#         print("测试开始")
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(20)
#         self.base_url = "http://xdclass.net"
#         self.driver.get(self.base_url)
#
#
#     def tearDown(self):
#         print("单个测试用例结束")
#         pass
#
#
#
#     def test_login(self):
#         u"登录测试案例"
#         driver = self.driver
#
#         login_ele = "#app > div > div.header > div > div.r_userinfo.f_r > div.login > span:nth-child(2)"
#         driver.find_element_by_css_selector(login_ele).click()
#         sleep(2)
#         user_name = "#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]"
#         pwd = "#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]"
#         driver.find_element_by_css_selector(user_name).clear()
#         driver.find_element_by_css_selector(user_name).send_keys("16621103980")
#         sleep(1)
#         driver.find_element_by_css_selector(pwd).clear()
#         driver.find_element_by_css_selector(pwd).send_keys("123456789")
#
#         login_btn_ele = driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.login_btn > button")
#         login_btn_ele.click()
#
#         # # user_info_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.avatar.f_r > img")
#         # sleep(1)
#         # # ActionChains(driver).move_to_element(user_info_ele).perform()
#         # sleep(1)
#         #获取用户名称元素
#         user_name_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.userbox.f_r > div > div.user > p")
#         print("测试结果")
#         print(user_name_ele.text)
#
#
#         # name = user_name_ele.text
#         sleep(2)
#         video_ele = driver.find_element_by_css_selector("#app > div > div.hot > div > div.content > a:nth-child(1) > div > img")
#         video_ele.click()
#         sleep(2)
#         #通过索引切换窗口
#         windows =driver.window_handles
#         driver.switch_to.window(windows[-1])
#
#         buy_btn_ele = driver.find_element_by_css_selector("#app > div > div.details_container.clearfix > div.body.w > div.r_container.f_r > div.gostudy > div.buy_tolearn > a")
#         buy_btn_ele.click()
#         print("进入下单页面")
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()


# import unittest
# import HTMLTestRunner
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
#
# class XdclassTestCase(unittest.TestCase):
#     def setUp(self):
#         print("测试开始")
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(20)
#         self.base_url = "http://xdclass.net"
#         self.driver.get(self.base_url)
#
#     def tearDown(self):
#         print("单个测试用例结束")
#         pass
#
#     def test_login(self):
#         u"登录测试案例"
#         driver = self.driver
#
#         login_ele = "#app > div > div.header > div > div.r_userinfo.f_r > div.login > span:nth-child(2)"
#         driver.find_element_by_css_selector(login_ele).click()
#         sleep(2)
#         user_name = "#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]"
#         pwd = "#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]"
#         driver.find_element_by_css_selector(user_name).clear()
#         driver.find_element_by_css_selector(user_name).send_keys("16621103980")
#         sleep(1)
#         driver.find_element_by_css_selector(pwd).clear()
#         driver.find_element_by_css_selector(pwd).send_keys("123456789")
#
#         login_btn_ele = driver.find_element_by_css_selector(
#             "#app > div > div.header > div.main > div.login > div > div.login_btn > button")
#         login_btn_ele.click()
#
#         # # user_info_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.avatar.f_r > img")
#         # sleep(1)
#         # # ActionChains(driver).move_to_element(user_info_ele).perform()
#         # sleep(1)
#         # 获取用户名称元素
#         user_name_ele = driver.find_element_by_css_selector(
#             "#app > div > div.header > div > div.userbox.f_r > div > div.user > p")
#         print("测试结果")
#         print(user_name_ele.text)
#
#         # name = user_name_ele.text
#         sleep(2)
#         video_ele = driver.find_element_by_css_selector(
#             "#app > div > div.hot > div > div.content > a:nth-child(1) > div > img")
#         video_ele.click()
#         sleep(2)
#         # 通过索引切换窗口
#         windows = driver.window_handles
#         driver.switch_to.window(windows[-1])
#
#         buy_btn_ele = driver.find_element_by_css_selector(
#             "#app > div > div.details_container.clearfix > div.body.w > div.r_container.f_r > div.gostudy > div.buy_tolearn > a")
#         buy_btn_ele.click()
#         print("进入下单页面")
#
#
#     def test_move(self):
#         self.driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)").click()
#         sleep(1)
#         self.driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.innerbox > div.video_card > a:nth-child(1) > div > img").click()
#         print("完成")
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(XdclassTestCase('test_login'))
#     suite.addTest(XdclassTestCase('test_move'))
#
#     file_prefix = time.strftime("%Y.%m.%d %H_%M_%S", time.localtime())
#     print(file_prefix)
#     file_name = "D:" + file_prefix + "result.html"
#     fp = open(file_name, "wb")
#     # stream  定义一个测试报告写入的文件，title就是标题，description就是描述
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"小D课堂 测试报告", description=u"测试用例执行情况")
#     runner.run(suite)
#     fp.close()





#发送邮件


"""
1.使用126邮箱，http://mail.126.com
A:waitforxy@126.com
B:waitfordev@126.com
POP3服务器： pop.126.com    110
SMTP服务器： smtp.126.com   25
IMAP服务器： imap.126.com   143
"""

# import smtplib
# import os,time,datetime
# from email.mime.text import MIMEText
# from email.header import Header
#
#
# #收件人
# sender = "xiaozhenjie5221@163.com"
# receiver = "963179571@qq.com"
#
# #不用密码发送，而是用授权码
# auth_code = "jienuo1314"
# subject = "自动化测试报告"
#
# #定义发送内容
# msg = MIMEText("<html><h2>欢迎来带小D课堂<h2><html>",_subtype="html",_charset="utf-8")
# msg["Subject"] = subject
# msg["from"] = sender
# msg["to"] = receiver
#
#
# smtp = smtplib.SMTP()
# smtp.connect("smtp.163.com")
# smtp.login(sender,auth_code)
# smtp.sendmail(sender,receiver,msg.as_string())
#
# smtp.quit()





# 发送附件
import smtplib
import os,time,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


#收件人
sender = "xiaozhenjie5221@163.com"
receiver = "963179571@qq.com"

#不用密码发送，而是用授权码
auth_code = "jienuo1314"
subject = "自动化测试报告"


f = open("D://2019.08.10 18_25_48result.html",'rb')
mail_body = f.read()
print(mail_body)
f.close()


#HTML形式的文件内容
html = MIMEText(mail_body,_subtype="html",_charset="utf-8")
html["Subject"] = subject
html["from"] = sender
html["to"] = receiver


# html附件  将测试报告放在附件中发送
att1 = MIMEText(mail_body,'base64','gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="report.html"'



msg = MIMEMultipart()
msg["Subject"] = subject
msg.attach(html)
msg.attach(att1)



# 连上服务器
smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login(sender,auth_code)
smtp.sendmail(sender,receiver,msg.as_string())

smtp.quit()