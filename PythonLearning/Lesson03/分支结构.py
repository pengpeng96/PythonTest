'''
学习内容：
分支结构的应用场景
    1。程序中的判断
        if 微信密码正确：
        登录到界面
        else:
            请重新输入密码
    2。判断定义： 如果 条件满足，才能做某件事情，
        如果 条件不满足，就做另外一件事情，或者什么也不做
        判断语句 又被称为 “分支语句”，正是因为有了判断，才让程序有了很多的分支
    3.if 判断语句基本语法
        在 Python 中，if 语句 就是用来进行判断的，格式如下：
        if 要判断的条件:
            条件成立时，要做的事情
            ……

if 条件:
    if语句块
   执行流程:判断条件是否为真. 如果真. 执行if语句块
        例子如下：
        1 money = int(input('请输入你兜里的钱:'))
        2 if money >500:
        3     print("吃烧烤")  # 只看缩进结果

注意：代码的缩进为一个 tab 键，或者 4 个空格 —— 建议使用空格
在 Python 开发中，Tab 和空格不要混用！
我们可以把整个 if 语句看成一个完整的代码块
if 语句以及缩进部分是一个 完整的代码块
else 处理条件不满足的情况

if 要判断的条件:
条件成立时，要做的事情
……
else:
条件不成立时，要做的事情
……
if 和 else 语句以及各自的缩进部分共同是一个 完整的代码块

例子如下：
    money = int(input('请输入你兜里的钱:'))
if money >500:
    print("吃烧烤")  # 只看缩进结果
    print("喝啤酒")  # 在同一个缩进的是一个语句块
    print("找好朋友聊聊天")
else: #否则.条件不成立
    print('吃泡面')
    print('盖浇饭')
    print('老干妈+馒头')



    4.逻辑运算
        在程序开发中，通常 在判断条件时，会需要同时判断多个条件
        只有多个条件都满足，才能够执行后续代码，这个时候需要使用到 逻辑运算符*
        逻辑运算符 可以把 多个条件 按照 逻辑 进行 连接，变成 更复杂的条件
        Python 中的 逻辑运算符 包括：与 and／或 or／非 not 三种
    and：条件1 and 条件2
        与／并且
        两个条件同时满足，返回 True
        只要有一个不满足，就返回 False
        or：条件1 or 条件2
        或／或者
        两个条件只要有一个满足，返回 True
        两个条件都不满足，返回 False
        not：not条件
        非/不是

    5.if 语句进阶
        在开发中，使用 if 可以 判断条件
        使用 else 可以处理 条件不成立 的情况
        但是，如果希望 再增加一些条件，条件不同，需要执行的代码也不同 时，就可以使用 elif
            语法格式如下：

                if 条件1:
                    条件1满足执行的代码
                    ……
                elif 条件2:
                    条件2满足时，执行的代码
                ……
                elif 条件3:
                    条件3满足时，执行的代码
                    ……
                else:
                    以上条件都不满足时，执行的代码
                    ……

            对比逻辑运算符的代码
                if 条件1 and 条件2:
                    条件1满足 并且 条件2满足 执行的代码
                        ……


            score = int(input("请输入你的分数"))
            if score >= 90:
                print("优秀")
            elif score >=80:
                 print("良好")
            elif score >=70:
                print("中等")
            elif score >=60:
            print("及格")
            else:
                 print("不及格")

        注意
        1.elif 和 else 都必须和 if 联合使用，而不能单独使用
        2. 可以将 if、elif 和 else 以及各自缩进的代码，看成一个 完整的代码块


    6.if 的嵌套
        elif 的应用场景是：同时 判断 多个条件，所有的条件是 平级 的
        在开发中，使用 if 进行条件判断，如果希望 在条件成立的执行语句中 再 增加条件判断，就可以使用 if 的嵌套
        if 的嵌套 的应用场景就是：在之前条件满足的前提下，再增加额外的判断
        if 的嵌套 的语法格式，除了缩进之外 和之前的没有区别

        if 条件 1:
            条件 1 满足执行的代码
            ……

        if 条件 1 基础上的条件 2:
            条件 2 满足时，执行的代码
            ……

        else:
            条件 2 不满足时，执行的代码

        else:
            条件1 不满足时，执行的代码
            ……


        if 嵌套
             if 条件:
                 if 条件:
                 ..
                else:
                    if 条件:
                     ...

             PS: 嵌套的层数不要太多,一般不超过3-5层

if嵌套的例子如下：

print("咣咣咣")
gender = input("请输入你的性别:")
if gender == "男": # = 赋值 ==判断
    print("去隔壁.alex等着你")
else: # 不是男
    ask = input("请问是不是包租婆?")
    if ask == '是':
        print("去隔壁,alex等着你,wusir也在!")
    else:# 不是包租婆
        height = int(input("请问你多高了"))
        if height > 200:
            print("太可怕了.去隔壁.去隔壁")
        else:
            print("请进.我家的西瓜.又大又甜!")





'''