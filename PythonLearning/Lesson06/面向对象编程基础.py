'''
学习内容：
类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / __str__方法
使用对象 - 创建对象 / 给对象发消息
面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
类中的方法 - 实例方法 / 类方法 / 静态方法
继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 /
本周六提交学习笔记。  基础部分马上就要结束了，希望大家好好完成本次作业。这些内容这些内容已经能能够适应自动化测试的85%以上的要求了。
所以本周日进行总结。每个人把之前所学内容都进行一次总结回顾。

'''

# 面向对象编程基础
'''
什么是面向对象编程?
把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，
通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。
这样一说是不是更不明白了。所以我们还是看看更通俗易懂的说法

面向对象(Object Oriented,OO)是软件开发方法。面向对象的概念和应用已超越了程序设计和软件开发，扩展到如数据库系统、交互式界面、
应用结构、应用平台、分布式系统、网络管理结构、CAD技术、人工智能等领域。面向对象是一种对现实世界理解和抽象的方法，是计算机编程技术
发展到一定阶段后的产物。核心特性包括：类，对象，方法，封装，继承和多态。


#类和对象

简单的说，类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，
而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。
当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。


对象和类的关系：
类与对象的关系就如模具和铸件的关系，类的实力化的结果就是对象，而对对象的抽象就是类，类描述了一组有相同特性（属性）和相同行为的对象。

解释的通俗一点就是，人是一种类，而具体的某一个人就是一个对象，每一个对象都符合这个类型的标准。

一个类的所有对象都有相同的属性（都是人类），但有不同的属性值（名字、身高不一样等），不同的类的属性不完全相同。

'''
# 定义类
# # 在Python中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。
# class Student(object):
#     # __init__是一个特殊方法用于在创建对象时进行初始化操作
#     # 通过这个方法我们可以为学生对象绑定name和age两个属性
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def study(self,course_name):
#         print('%s正在学习%s.' % (self.name,course_name))
#
#     # PEP 8要求标识符的名字用全小写多个单词用下划线连接
#     # 但是很多程序员和公司更倾向于使用驼峰命名法（驼峰标识）
#     def watch_video(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看仙侠电视剧' %  self.name)
#
# # *说明*：写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。
#
# # 创建和使用对象
# # 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。
# def main():
#     # 创建学生对象并指定姓名和年龄
#     stu1 = Student('彭彭',23)
#     # 给对象发送study消息
#     stu1.study('Python程序设计')
#     # 给对象发送watch_video消息
#     stu1.watch_video()
#     stu2 = Student('王大锤',18)
#     stu2.study('Java程序设计')
#     stu2.watch_video()
#
# if __name__ == '__main__':
#     main()

# # 定义类----通过class关键字
# class Student(object):
#     pass
# # class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们
# # 后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#
# # 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
# bart = Student()
# print(bart)
# print(Student)
# # 可以看到，变量bart指向的就是一个Student的实例，后面的0x0000022D76F16470是内存地址，每个object的地址都不一样，而Student本身则是一个类。
# # 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
#
# bart.name = 'Bart Simpson'
# print(bart.name)
#
# # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，
# # 在创建实例的时候，就把name，score等属性绑上去：
#
# class Student(object):
#
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# #      注意：特殊方法“__init__”前后分别有两个下划线！！！
#
# bart = Student('Jack',78)
# print(bart.name)
# print(bart.score)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，
# 类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。


# 类的基本结构
'''
创建出来的 对象 叫做 类 的 实例
创建对象的 动作 叫做 实例化
对象的属性 叫做 实例属性
对象调用的方法 叫做 实例方法

在程序执行时：
对象各自拥有自己的 实例属性
调用对象方法，可以通过 self.
访问自己的属性
调用自己的方法

结论
每一个对象 都有自己 独立的内存空间，保存各自不同的属性
多个对象的方法，在内存中只有一份，在调用方法时，需要把对象的引用 传递到方法内部

'''
# class Tool(object):
#     # 利用赋值语句定义类属性，记录数量
#     count = 0
#
#     def __init__(self,name):
#         self.name = name
#         # 类属性 --- 类结构+1
#         Tool.count += 1
#
# # 创建对象
# tool1 = Tool('斧子')
# tool2 = Tool('剪刀')
# tool3 = Tool('锄头')
# # 使用类名.属性名 -- 获取数量
# print(Tool.count)

# 类的属性和方法
'''
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用self.__private_methods
'''
# #coding=utf-8
# #!/usr/bin/python
#
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0    # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量,可以使用 object._className__attrName 访问属性
# object._className__secretCount
# print(counter._JustCounter__secretCount)


# Python构造器
'''
 类的构造器
__init__ 构造函数，在生成对象时调用。由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制
填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把 name score 等属性上去。默认的属性可以写在__init__ 下面。
'''
# # /usr/bin/python
# # coding = utf-8
# class ren(object):
# # def _init__类的默认属性。当实例化类的时候，就会调用默认属性
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#         def funC(self):
#             print('hello[0]'.format(self.name))
# #           实例化类.__init__是一个构造器（初始化），当你实例化这个类的时候，必须输入name和sex变量
#         test = ren('pj','R')
#         test.funC()




# 构析器
# # __del__是析构器，当Python对象的所有引用都不存在了（被del了），就会自动触发__del__执行。
# class CapStr(str):
#     def __new__(cls, string):   # 此时string = 'i love you' cls是CapStr这个类的对象
#         string = string.upper()
#         return str.__new__(cls. string)   # 返回cls类带string参数的实例化的对象,但是这里为什么不直接return string ？看下面的代码段
#     def __del__(self):
#         print('__del__析构方法被调用了！')
#
# a = CapStr('i love you')
# b = a
# c = b
# del c
# del a
# del b


# #  __str__方法
# class Cat:
#     """定义一个猫类"""
#
#     def __init__(self, new_name, new_age):
#         """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
#         # self.name = "汤姆"
#         # self.age = 23
#         self.name = new_name
#         self.age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
#         # num = 100  # 它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,因此其他方法不能使用这个变量
#
#     def __str__(self):
#         """返回一个对象的描述信息"""
#         # print(num)
#         return "名字是:%s , 年龄是:%d" % (self.name, self.age)
#
#     def eat(self):
#         print("%s在吃鱼仔...." % self.name)
#
#     def drink(self):
#         print("%s在喝雪碧..." % self.name)
#
#     def introduce(self):
#         # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
#         # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
#         print("名字是:%s, 年龄是:%d" % (self.name, self.age))
#
#
# # 创建了一个对象
# tom = Cat("汤姆", 23)
# print(tom)

'''
在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描写
'''


'''
### 面向对象的四大支柱

面向对象有四大支柱：抽象、封装、继承和多态。我自己对封装的理解是“隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口”。
我们在类中定义的方法其实就是把数据和对数据的操作封装起来了，在我们创建了对象之后，只需要给对象发送一个消息（调用方法）就可以
执行方法中的代码，也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图），而不需要知道方法内部的实现细节（方法的内部视图）。
'''


# 抽象:抽象就是忽略一个主题中与当前目标无关的方面,以便更充分的注意与当前目标有关的方面
#
# 继承:继承是一种联结的层次模型,并且鼓励类的重用,它提供了明确的表述共性的方法.对象的一个新类可以从现有的类中派生
#
# 封装:封装是把过程和数据包围起来,对数据的访问只能通过已定义的界面,实现一个完全自制 封装的对象
#
# 多态:不同类的对象对同一消息作出相应,包括参数化多态性和包含多态性


# 抽象
# # 抽象方法
# class Person():
#     def say(self):
#         pass
# class Student(Person):
#     def say(self):
#         print("i am student")

'''
抽象类： 包含抽象方法的类

抽象类可以包含非抽象方法
抽象类可以有方法和属性
抽象类不能进行实例化
必须继承才能使用，且继承的子类必须实现所有抽象方法

'''
# import abc
# class Person(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def say(self):
#         pass
# class Student(Person):
#     def say(self):
#         print("i am student")
#     s = Student()
#     s.say()
#
# # 补充：函数名和当做变量使用
# class Student():
#     pass
# def say(self):
#     print("i am say")
# s = Student()
# s.say = say
# s.say(9)
#
# # 组装类
# from types import MethodType
# class Student():
#     pass
# def say(self):
#     print("i am say")
# s = Student()
# s.say = MethodType(say,Student)
# s.say()
#
# # 元类
# # 类名一般为MetaClass结尾
# class StudentMetaClass(type):
#     def __new__(cls, *args, **kwargs):
#         print("元类")
#         return type.__new__(cls, *args, **kwargs)
# class Teacher(object,metaclass= StudentMetaClass):
#     pass
# t = Teacher()
# print(t.__dict__)


# 附：python 抽象类、抽象方法的实现示例
#
# 由于python 没有抽象类、接口的概念，所以要实现这种功能得abc.py 这个类库,具体方式如下

# from abc import ABCMeta,abstractmethod
# # 抽象类
# class Headers(object):
#     __metaclass__ = ABCMeta
#     def __init__(self):
#         self.headers = ''
#     @abstractmethod
#     def _getBaiduHeaders(self):pass
#     def __str__(self):
#         return str(self.headers)
#     def __repr__(self):
#         return repr(self.headers)
#
# # 实现类
# class BaiduHeaders(Headers):
#     def __init__(self,url,username,password):
#         self.url = url
#         self.headers = self._getBaiduHeaders()
#     def _getBaiduHeaders(self,username,password):
#         client = GLOBAL_SUDS_CLIENT.client(self.url)
#         headers = client.factory.create('ns0:AuthHeader')
#         headers.username = username
#         headers.password = password
#         headers.token = _baidu_headers['token']
#         return headers

# 如果子类不实现父类的_getBaiduHeaders方法,则抛出TypeError:
#  Can't instantiate abstract class BaiduHeaders with abstract methods  异常



#封装
#1.将属性和方法封装到一个抽象的类中
#2.外界使用类创建对象，对象调用方法
#3.对象方法的细节都被封装在类的内部

# 封装，顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容。
# 对于面向对象的封装来说，其实就是使用构造方法将内容封装到 对象 中，然后通过对象直接或者self间接获取被封装的内容。

# 通过对象直接调用被封装的内容
# class Foo:
#       def __init__(self,name,age):
#           self.name = name
#           self.age = age
#
# obj1 = Foo('xiaopeng',18)
# print(obj1.name)  # 直接调用obj1对象的name属性
# print(obj1.age)  # 直接调用obj1对象的age属性
#
# obj2 = Foo('xiaoming',20)
# print(obj2.name)  # 直接调用obj2对象的name属性
# print(obj2.age)  # 直接调用obj2对象的age属性
#
#
# # 通过self间接调用
# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
# # Python默认会将obj1传给self参数，即：obj1.detail(obj1)，所以，此时方法内部的 self ＝ obj1，
# # 即：self.name 是 xiaoming ；self.age 是 18
# obj1 = Foo('xiaoming', 28)
# obj1.detail()
#
# # Python默认会将obj2传给self参数，即：obj1.detail(obj2)，所以，此时方法内部的 self ＝ obj2，
# # 即：self.name 是 xiaohe ； self.age 是 78
# obj2 = Foo('xiaohe', 30)
# obj2.detail()

'''
需求
1.李雷体重75.0公斤
2.李雷每次跑步会减肥0.5公斤
3.李雷每次吃东西体重会增加1公斤

需求
1.李雷和韩梅梅都爱跑步
2.韩梅梅体重45.0公斤
3.李雷体重75.0公斤
4.每次跑步都会减少0.5公斤
5.每次吃东西都会增加1公斤


'''
# class Person():
#
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return '我的名字叫 %s 体重是 %.2f' %(self.name,self.weight)
#
#     def run(self):
#         print('%s爱跑步' %self.name)
#         self.weight -= 0.5
#
#     def eat(self):
#         print('%s吃东西' %self.name)
#         self.weight += 1
#
# Lilei = Person('李雷',75.0)
# Lilei.run()
# print(Lilei)
# Lilei.eat()
# print(Lilei)


# 继承
# 1.封装：根据职责将属性和方法封装到一个抽象的类中
# 2.继承：实现代码的重用，相同的代码不需要重复的写
# #子类继承自父类，可以直接享受父类中已经封装好的方法
# #子类中应该根据职责，封装子类特有的属性和方法
# class Animal():
#
#     def eat(self):
#         print('吃')
#
#     def drink(self):
#         print('喝')
#
#     def run(self):
#         print('跑')
#
#     def sleep(self):
#         print('睡')
#
# class Cat(Animal):	#定义Cat类继承Animal类的动作
#     # def eat(self):
#     #     print('吃')
#     #
#     # def drink(self):
#     #     print('喝')
#     #
#     # def run(self):
#     #     print('跑')
#     #
#     # def sleep(self):
#     #     print('睡')
#     def shout(self):
#         print('喵')
#
# fentiao = Cat()
# fentiao.eat()
# fentiao.drink()
# fentiao.run()
# fentiao.sleep()
# fentiao.shout()




#子类可以继承父类的所有属性和方法
#继承具有传递性，子类拥有父类的父类的属性和方法
# class Animal():
#
#     def eat(self):
#         print('吃')
#
#     def drink(self):
#         print('喝')
#
#     def run(self):
#         print('跑')
#
#     def sleep(self):
#         print('睡')
#
# class Cat(Animal):
#     def shout(self):
#         print('喵')
#
#
# class Hellokitty(Cat):
#     def speak(self):
#         print('我会说日语')
#
# class Dog(Animal):
#     def bark(self):
#         print('汪')
#
# kt = Hellokitty()
# kt.speak()
#
# kt.shout()
#
# kt.eat()
# kt.sleep()


# 当父类方法不能满足子类的需求时，可以对方法进行重写
# 1.覆盖父类的方法
# 2.对父类的方法进行扩展
# #如果子类中，重写了父类的方法
# #在运行时，只会调用在子类中重写的方法
# class Animal():
#
#     def eat(self):
#         print('吃')
#
#     def drink(self):
#         print('喝')
#
#     def run(self):
#         print('跑')
#
#     def sleep(self):
#         print('睡')
#
# class Cat(Animal):
#     def shout(self):
#         print('喵')
#
# class Hellokitty(Cat):
#     def speak(self):
#         print('我可以说日语')
#     def shout(self):
#         print('@#$%%@$#@#@$')
#
# kt = Hellokitty()
#
# kt.shout()



# class A():
#     def test(self):
#         print('A --- test方法')
#     def demo(self):
#         print('A --- demo方法')
#
# class B():
#     def test(self):
#         print('B --- test 方法')
#     def demo(self):
#         print('B --- demo方法')
#
# class C(A,B):	# C类继承了A和B两个类，运行结果为A类的结果，因为A类在前
#     pass
#
# c = C()
# c.test()
# c.demo()

# 运行结果：
# A --- test方法
# A --- demo方法



# 多态
# 子类和父类存在相同方法时，子类会覆盖父类方法
# #运行时总会调用子类方法–> 多态
# 多态是以封装和继承为前提的
# 如果子类不同那么调用相同的方法也会产生不同的执行结果
# class Animal(object):
#     def run(self):
#         print('running...')
#     def cry(self):
#         print('crying...')
#
# class Dog(Animal):
#     def run(self):
#         print('dog running...')
#
#     def eat(self):
#         print('dog eating...')
#
# class Cat(Animal):
#     def run(self):
#         print('cat running...')
#
# cat = Cat()
# cat.run()
#
# dog = Dog()
# dog.run()

# 运行结果：
# cat running...
# dog running...




'''
类：对具有相同数据和方法的一组对象的描述或定义。
对象：对象是一个类的实例。
实例(instance)：一个对象的实例化实现。
标识(identity)：每个对象的实例都需要一个可以唯一标识这个实例的标记。
实例属性（instance attribute）：一个对象就是一组属性的集合。
实例方法(instance method)：所有存取或者更新对象某个实例一条或者多条属性的函数的集合。
类属性（classattribute）：属于一个类中所有对象的属性，不会只在某个实例上发生变化
类方法（classmethod）：那些无须特定的对性实例就能够工作的从属于类的函数。


类是一个特殊的对象
python中一切皆对象
    class AAA： 定义的类属性属于类对象
    obj1 =AAA： 属于实例对象
在运行程序时，类 同样会被加载到内存
在python中，类是一种特殊的对象    类对象
除了封装 实例（对象） 的属性和方法外，类对象还可以有自己的属性和方法
通过类名. 的方式可以直接访问类的属性或者调用类的方法


class Tool(object):
    # 1使用赋值语句定义类属性，记录所有工具的数量
    count = 0
    def __init__(self,name):
        self.name = name
        # 类属性值+1
        Tool.count += 1
# 创建工具对象（在创建对象的时候，会自动调用初始化方法）
tool1 = Tool('斧子')
tool2 = Tool('钳子')
tool3 = Tool('榔头')
# 输出工具对象的总数
# 使用类明.属性名 来获取
print  Tool.count


'''

# 实例属性和类属性
# 实例属性通过self或实例变量来定义，注意__init__方法中定义的是实例属性
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
# s1 = Student('Bob')
# #给实例添加一个属性
# s1.score = 90
#
# s2 = Student('Jim')
#
# # 在实例s1中添加一个属性score, 该属性只对s1有用，在s2中是没有的
# s1.score
# s2.score

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'
#

# # 类属性是怎么定义的呢？
# class Student(object):
#     name = 'Student'
# # 当我们定义一个类属性后，这个属性归类所有，所有的实例都可以访问它
# s1 = Student()
# s2 = Student()
# print(s1.name,s2.name)
#
# # 现在修改一个s1的name, 会出现什么情况呢？
# s1.name = 'windows'
# print(s1.name)
# print(s2.name)
# # 再删除s1的那么属性
# del s1.name
# print(s1.name)
#
# # 需要用到@property装饰器，来把方法变成属性
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score ust between 0 ~ 100!')
#         self._score = value
#
# # 这样就可以像属性一样操作了：
# s = Student()
# s.score = 60
# print(s.score)
# print(s.score = 9999)

# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!



### @property装饰器

# 之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
# 比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，
# 不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。如果要做到这点，
# 就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '王尼玛'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()


### 使用__slots__

# 我们讲到这里，不知道大家是否已经意识到,通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性
# 和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义\_\_slots\_\_变量来进行限定。
# 需要注意的是\_\_slots\_\_的限定只对当前类的对象生效，对子类并不起任何作用。


class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 23)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True





### 静态方法和类方法

# 之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。实际上，我们写在类中的方法并不需要都是对象方法，
# 例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，
# 因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来
# （因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


if __name__ == '__main__':
    main()


# 和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象
# （类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，
# 代码如下所示。

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()


'''
### 类之间的关系

# 简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

# - is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
# - has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；
如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
# - use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。

# 我们可以使用一种叫做[UML]（统一建模语言）的东西来进行面向对象建模，其中一项重要的工作就是把类和类之间的关系用标准化的图形符号描述出来。
关于UML我们在这里不做详细的介绍，有兴趣的读者可以自行阅读[《UML面向对象设计基础》](https://e.jd.com/30392949.html)一书。

# 利用类之间的这些关系，我们可以在已有类的基础上来完成某些操作，也可以在已有类的基础上创建新的类，这些都是实现代码复用的重要手段。
复用现有的代码不仅可以减少开发的工作量，也有利于代码的管理和维护，这是我们在日常工作中都会使用到的技术手段。



### 继承和多态
# 刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复
代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。子类除了继承父类提供的
属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象，
这是面向对象编程中一个常见的行为，对应的原则称之为[里氏替换原则]。下面我们先看一个继承的例子。

'''

class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看古装动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('彭彭', 23, '小白')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()


# 子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
# 通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
# 不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('大黄'), Dog('二黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()

'''
在上面的代码中，我们将`Pet`类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来
达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类
中的`make_voice`抽象方法进行了重写并给出了不同的实现版本，当我们在`main`函数中调用该方法时，这个方法就表现出了多态行为
（同样的方法做了不同的事情）。

'''

