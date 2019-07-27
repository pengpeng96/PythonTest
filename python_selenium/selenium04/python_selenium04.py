# 第五章 selenium实战之模拟事件处理

'''
# 1、自动化测试实战之ActionChains模拟用户行为
    简介：讲解使用selenium里面的ActionChains模拟用户的行为

    需求：
        需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽

    解决：selenium提供了一个类来处理这类事件
    selenium.webdriver.common.action_chains ActionChains(driver)

    脚本：
        from selenium.webdriver.common.action_chains import ActionChains

    执行原理：
        调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列里，
        当调用perform()方法时，队列中的事件会依次执行

    支持链式写法或者分步写法
    ActionChains(driver).click(ele).perform()

    鼠标和键盘方法列表：
        perform()  执行链中的所有动作
        click(on_element=None)  单击鼠标左键
        context_click(on_element=None)  点击鼠标右键
        double_click(on_element=None)   双击鼠标左键
        move_to_element(to_element)   鼠标移动到某个元素
        ele.send_keys(keys_to_send)   发送某个词到当前焦点的元素

    不常用的方法列表：
        （1）click_and_hold(on_element=None)　　点击鼠标左键,不松开
        （2）release(on_element=None)　　在某个元素位置松开鼠标左键
        （3）key_down(value,element=None)　　按下键盘上的某个键
        （4）key_up(value,element=None)　　松开键盘上的某个键
        （5）drag_and_drop(source,target)　　拖拽到某个元素然后松开
        （6）drag_and_drop_by_offset(source,xoffset,yoffset)　　拖拽到某个坐标然后松开
        （7）move_by_offset(xoffset,yoffset)　　鼠标从当前位置移动到某个坐标
        （8）move_to_element_with_offset(to_element,xoffset,yoffset)　　移动到距某个元素（左上角坐标）多少距离的位置　　



# 2、鼠标事件实战之hover菜单栏弹出

     简介：鼠标事件之菜单栏hover弹出

     1.引入ActionChains类
     from selenium.webdriver.common.action_chains import ActionChains

     2.move_toelement(to_element)  鼠标移动到某个元素

     对定位到的元素执行鼠标移动到上面的操作
     ActionChains(driver).move_to_element(ele1).perform()


'''

# 菜单栏弹出例子练习1
# --*--coding:-utf-8--*--
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

# 拿到driver
driver = webdriver.Chrome()

# 跳转网页
driver.get('https://xdclass.net')

print(driver.title)

# 睡眠时间3秒
sleep(3)

# 定位鼠标移动到上面的元素
menu_ele = driver.find_element_by_css_selector('#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)')
ActionChains(driver).move_to_element(menu_ele).perform()

# 选中子菜单
sub_menu_ele = driver.find_element_by_css_selector('#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(1)')
sleep(2)
sub_menu_ele.click()


# 菜单栏弹出例子练习2
# --*--coding:-utf-8--*--
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

url = 'https://www.imooc.com'
broswer = webdriver.Firefox()
broswer.get(url)
sleep(3)
print(broswer.title)
# 定位鼠标移动到上面的元素
positionTest = broswer.find_element_by_css_selector("div.item:nth-child(6) > a:nth-child(1) > span:nth-child(1)")
ActionChains(broswer).move_to_element(positionTest).perform()
sleep(3)
# 选中子菜单
positionAutotest = broswer.find_element_by_css_selector("div.submenu:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(9)")
positionAutotest.click()




# 3、多知识点综合实战之模拟用户登录

    # 简介：讲解使用selenium模拟登录小D课堂，并选择课程
    # （1）多知识点实战
    # （2）查找登录_——》输入用户名和密码——》触发登录——》判断登录是否成功——》打印结果


# --*--coding:-utf-8--*--
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

# 拿到driver
driver = webdriver.Firefox()

# 跳转网页
driver.get('https://xdclass.net')

print(driver.title)

# 睡眠时间3秒
sleep(3)

# 查找登录框
login_ele = driver.find_element_by_css_selector('.login > span:nth-child(2)')

#触发点击事件
ActionChains(driver).click(login_ele).perform()

# 查找输入框，输入账号密码，输入框需要提前清理
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("13602694157")
driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("peng12345678")
# 点击登录
driver.find_element_by_css_selector(".btn").click()

# 判断是否登录成功
# 将鼠标移动到头像，判断弹窗字符
sleep(5)
use_info_ele = driver.find_element_by_css_selector(".avatar_img")

# 触发hover事件
ActionChains(driver).move_to_element(use_info_ele).perform()

# 获取用户名的元素
user_name_ele = driver.find_element_by_css_selector('.username')

print('====测试结果===')
print(user_name_ele.text)

name = user_name_ele.text

if name == 'pengpeng':
    print('登录成功')
else:
    print('登录失败')





'''
# 4、自动化测试实战之网页等待时间
     简介：讲解自动化测试的等待时间
     
     1.为什么需要等待时间——>等系统稳定
     网页需要加载对应的资源文件，页面渲染，窗口处理等等
     
     2.自动化测试常用的等待时间
        强制等待：(自己调试代码看效果，开发调试代码比较常用)
         from time import sleep
         sleep(5)  # 强制等待5秒再执行下一步，缺点是不管资源是否完成，都必须等待
        
        隐性等待：(一般工作中使用隐形等待)
          driver.implicitly_wait(10)  # 隐性等待，最长等10秒
          设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步否则一直等待时间截止，然后执行下一步
          缺点是程序会一直等待整个页面加载完成，到浏览器标签栏那个加载圈不在转
          
          注意：对driver起作用，所以设置一次即可，不用导出设置
         
         显性等待：(在元素出现时间较短，难以定位时使用)
          WebDriverWait 需要配合

          until和until_not 程序每隔N秒检查一次，如果成功，则执行下一步，否则继续等待，直到超过设置的最长时间
          from selenium.webdriver.support.wait import WebDriverWait
          
             语法：WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
                                    最长时间  每隔时间检查一次     忽略异常(非必须的)
               from selenium.webdriver.common.by import By
               from selenium.webdriver.support.ui import WebDriverWait
               from  selenium.webdriver.support import expected_conditions as EC
   
        结论：隐性等待和显性等待可以同时使用，等待的最长时间取两者之中的较大者
        
'''

# --*--coding:-utf-8--*--
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

# 拿到driver
driver = webdriver.Firefox()
driver.implicitly_wait(10)   # 隐形等待，最长等10秒
# 跳转网页
driver.get("https://baidu.com")

# 睡眠时间10秒
# sleep(10)

print(driver.title)


# --*--coding:-utf-8--*--
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

# 拿到driver
driver = webdriver.Firefox()
# driver.implicitly_wait(10)   # 隐形等待，最长等10秒

# 跳转网页
driver.get("https://baidu.com")

try:
    # 显性等待
    xian_xing = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    # 输入框输入小D课堂
    xian_xing.send_keys("小D课堂")
    driver.find_element_by_id('su').click()

    print("资源加载成功")

    print(driver.title)
except:
    print("资源加载失败，发送报警邮件或者短信")

# 不管有没有成功，都打印下，用于资源清理
finally:
    print("不管有没有成功，都打印下，用于资源清理")
    # 退出浏览器
    driver.quit()


