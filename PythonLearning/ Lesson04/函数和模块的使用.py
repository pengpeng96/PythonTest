'''
函数和模块的使用
在讲解本章节的内容之前，我们先来研究一道数学题，请说出下面的方程有多少组正整数解。
X1+X2+X3+X4=8
事实上，上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案。想到这一点问题的答案就呼之欲出了。

'''
# 输入M和N计算C(M,N)
m = int(input('m = '))
n = int(input('n = '))
sm = 1
for num in range(1,m+1):
    sm *= num
sn = 1
for num in range(1,n+1):
    sn *=num
smn = 1
for num in range(1,m-n-1):
    smn *=num
print(sm // sn // smn)


# 函数的作用
# 不知道大家是否注意到，在上面的代码中，我们做了3次求阶乘，这样的代码实际上就是重复代码。编程大师Martin Fowler先生曾经说过：“代码有很多种坏味道，
# 重复是最坏的一种！”，要写出高质量的代码首先要解决的就是重复代码的问题。对于上面的代码来说，我们可以将计算阶乘的功能封装到一个称之为“函数”的功能模块中，
# 在需要计算阶乘的地方，我们只需要“调用”这个“函数”就可以了。

### 定义函数
'''
在Python中可以使用`def`关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。
在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，
而函数执行完成后我们可以通过`return`关键字来返回一个值，这相当于数学上说的函数的因变量。
在了解了如何定义函数后，我们可以对上面的代码进行重构，所谓重构就是在不影响代码执行结果的前提下对代码的结构进行调整，
重构之后的代码如下所示。

'''
def factorial(num):
    '''
    求阶乘

    :param num:非负整数
    :return: num的阶乘
    '''
    result = 1
    for b in range(1,num+1):
        result *=b
    return result

a = int(input(' a = '))
b = int(input(' b = '))

# 当需要计算阶乘的时候不需要再写循环求阶乘，而只需要直接调用已经定义好的函数
print(factorial(a) // factorial(b) // factorial(a-b))


调用函数：
#    Python内置函数：
#    数学运算(15个): abs(x)                # 求绝对值:参数可以是整型，也可以是复数,若参数是复数，则返回复数的模
#                 complex([real[,imag]]) # 创建一个复数
#                 divmod(a,b)                # 分别取商和余数,注意：整型、浮点型都可以
#                 float([x])             # 将一个字符串或数转换为浮点数。如果无参数将返回0.0
#                 int([x[,base]])        #    将一个字符转换为int类型，base表示进制
#                 long([x[,base]])       # 将一个字符转换为long类型
#                 pow(x, y[,z])          # 返回x的y次幂
#                 range([start],stop[,step]) # 产生一个序列，默认从0开始
#                 round(x[,n])          # 四舍五入
#                 sum(iterable[,start])  # 对集合求和
#                 oct(x)                # 将一个数字转化为8进制
#                 hex(x)                # 将整数x转换为16进制字符串
#                 chr(i)                # 返回整数i对应的ASCII字符
#                 bin(x)                # 将整数x转换为二进制字符串
#                 bool([x])             # 将x转换为Boolean类型
#  集合类操作(15个):basestring()                   # str和unicode的超类，不能直接调用，可以用作isinstance判断
#                   format(value [, format_spec])      # 格式化输出字符串，格式化的参数顺序从0开始，如“I am {0},I like {1}”
#                   unichr(i)                          # 返回给定int类型的unicode
#                   enumerate(sequence [, start = 0])    # 返回一个可枚举的对象,该对象的next()方法将返回一个tuple
#                   iter(o[, sentinel])            # 生成一个对象的迭代器，第二个参数表示分隔符
#                   max(iterable[, args...][key])   # 返回集合中的最大值
#                   min(iterable[, args...][key])      # 返回集合中的最小值
#                   dict([arg])                    # 创建数据字典
#                   list([iterable])                   # 将一个集合类转换为另外一个集合类
#                   set()                              # set 对象实例化
#                   frozenset([iterable])              # 产生一个不可变的set
#                   str([object])                  # 转换为string类型
#                   sorted(iterable[, cmp[, key[, reverse]]])    # 队集合排序
#                   tuple([iterable])              # 生成一个tuple类型
#                   xrange([start], stop[, step])   # xrange()函数与range()类似,但xrnage()并不创建列表,而是返回一个xrange对象,
                                                  # 它的行为与列表相似,但是只在需要时才计算列表值,当列表很大时,这个特性能为我们节省内存
#   逻辑判断(3个):all(iterable) # 集合中的元素都为真的时候为真,特别的，若为空串返回为True
#                any(iterable)   # 集合中的元素有一个为真的时候为真,特别的，若为空串返回为False
#                cmp(x, y)       # 如果x < y ,返回负数；x == y, 返回0；x > y,返回正数
#   反射(33个)：callable(object)   # 检查对象object是否可调用
                                # 1、类是可以被调用的
                                # 2、实例是不可以被调用的，除非类中声明了__call__方法
              # classmethod()        # 1、注解，用来说明这个方式是个类方法
              #                   # 2、类方法即可被类调用，也可以被实例调用
              #                   # 3、类方法类似于Java中的static方法
              #                   # 4、类方法中不需要有self参数
              # compile(source,filename,mode[,flags[,dont_inherit]])
              #                   # 将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
              #                   # 1、参数source：字符串或者AST（Abstract Syntax Trees）对象。
              #                   # 2、参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
              #                   # 3、参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
              #                   # 4、参数flag和dont_inherit：这两个参数暂不介绍
              # dir([object])        # 1、不带参数时，返回当前范围内的变量、方法和定义的类型列表；
              #                   # 2、带参数时，返回参数的属性、方法列表。
              #                   # 3、如果参数包含方法__dir__()，该方法将被调用。当参数为实例时。
              #                   # 4、如果参数不包含__dir__()，该方法将最大限度地收集参数信息
              # delattr(object, name)    # 删除object对象名为name的属性
              # eval(expression [,globals [,locals]])    # 计算表达式expression的值
              # execfile(filename [,globals [,locals]])  # 用法类似exec()，不同的是execfile的参数filename为文件名，而exec的参数为字符串。
              # filter(function,iterable)    # 构造一个序列，等价于[ item for item in iterable if function(item)]
              #                  # 1、参数function：返回值为True或False的函数，可以为None
              #                  # 2、参数iterable：序列或可迭代对象
              # getattr(object, name [, defalut]) # 获取一个类的属性
              # globals()          # 返回一个描述当前全局符号表的字典
              # hasattr(object, name)    # 判断对象object是否包含名为name的特性
              # hash(object)    # 如果对象object为哈希表类型，返回对象object的哈希值
              # id(object)      # 返回对象的唯一标识
              # isinstance(object, classinfo)    # 判断object是否是class的实例
              # issubclass(class, classinfo) # 判断是否是子类
              # len(s)          # 返回集合长度
              # locals()            # 返回当前的变量列表
              # map(function, iterable, ...)     # 遍历每个元素，执行function操作
              # memoryview(obj)  # 返回一个内存镜像类型的对象
              # next(iterator[, default])    # 类似于iterator.next()
              # object()            # 基类
              # property([fget[, fset[, fdel[, doc]]]])  # 属性访问的包装类，设置后可以通过c.x=value等来访问setter和getter
              # reduce(function, iterable[, initializer])    # 合并操作，从第一个开始是前两个参数，然后是前两个的结果与第三个合并进行处理，以此类推
              # reload(module)   # 重新加载模块
              # setattr(object, name, value) # 设置属性值
              # repr(object)        # 将一个对象变幻为可打印的格式
              # slice（）  　
              # staticmethod    # 声明静态方法，是个注解
              # super(type[, object-or-type])    # 引用父类
              # type(object)     # 返回该object的类型
              # vars([object])   # 返回对象的变量，若无参数与dict()方法类似
              # bytearray([source [, encoding [, errors]]])  # 返回一个byte数组
                               # 1、如果source为整数，则返回一个长度为source的初始化数组；
                               # 2、如果source为字符串，则按照指定的encoding将字符串转换为字节序列；
                               # 3、如果source为可迭代类型，则元素必须为[0 ,255]中的整数；
              #                  # 4、如果source为与buffer接口一致的对象，则此对象也可以被用于初始化bytearray.
              # zip([iterable, ...]) # 实在是没有看懂，只是看到了矩阵的变幻方面
#   I/O操作(5个)：file(filename [, mode [, bufsize]])  # file类型的构造函数，作用为打开一个文件，如果文件不存在且mode为写或追加时，文件将被创建。添加‘b’到mode参数中，将对文件以二进制形式操作。添加‘+’到mode参数中，将允许对文件同时进行读写操作
                                                   # 1、参数filename：文件名称。
                                                   # 2、参数mode：'r'（读）、'w'（写）、'a'（追加）。
                #                                    # 3、参数bufsize：如果为0表示不进行缓冲，如果为1表示进行行缓冲，如果是一个大于1的数表示缓冲区的大小 。
                # input([prompt])    # 获取用户输入，推荐使用raw_input，因为该函数将不会捕获用户的错误输入
                # open(name[, mode[, buffering]])    # 打开文件，与file有什么不同？推荐使用open
                # print  # 打印函数
                # raw_input([prompt])    # 设置输入，输入都是作为字符串处理


                
# 函数的参数
'''
函数是绝大多数编程语言中都支持的一个代码的“构建块”，但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，
其中一个显著的区别就是Python对函数参数的处理。在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像
其他语言一样支持[函数的重载](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0%E9%87%8D%E8%BD%BD)，因为我们在定义一个函数的时候
可以让它有多种不同的使用方式，下面是两个小例子。

'''

from random import randint


def roll_dice(n=2):
    '''
    摇骰子

    :param n:骰子的个数
    :return: n颗骰子点数之和
    '''
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0,b=0,c=0):
    return a + b + c
# 如果没有指定参数就可以使用默认值摇两颗骰子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
# 传递参数时可不按照设定的顺序进行传递
print(add(c=50,a=100,b =200))

'''
我们给上面两个函数的参数都设定了默认值，这也就意味着如果在调用函数的时候如果没有传入对应参数的值时将使用该参数的默认值，
所以在上面的代码中我们可以用各种不同的方式去调用`add`函数，这跟其他很多语言中函数重载的效果是一致的。

其实上面的`add`函数还有更好的实现方案，因为我们可能会对0个或多个参数进行加法运算，而具体有多少个参数是由调用者来决定，
我们作为函数的设计者对这一点是一无所知的，因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示。
'''
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))
# print(add(2,4,6,8,10))


### 用模块管理函数
'''
对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，因为我们会遇到命名冲突这种尴尬的情况。
最简单的场景就是在同一个.py文件中定义了两个同名函数，由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味
着两个函数同名函数实际上只有一个是存在的。
'''

def foo():
    print('hello world！')

def foo():
    print('goodbye,world!')

foo()          #输出----goodbye,world!

'''
当然上面的这种情况我们很容易就能避免，但是如果项目是由多人协作进行团队开发的时候，团队中可能有多个程序员都定义了名为`foo`的
函数，那么怎么解决这种命名冲突呢？答案其实很简单，Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的
函数，在使用函数的时候我们通过`import`关键字导入指定的模块就可以区分到底要使用的是哪个模块中的`foo`函数，代码如下所示。
'''

'''
# module1.py

def foo():
    print('hello world!')

# module2.py

def foo():
    print('goodbye,world!')

# test.py

from module1 import foo
# 输出hello world!
foo()

from module2 import foo
# 输出goodbye,world!
foo()

也可以按照如下所示的方式来区分到底要使用哪一个`foo`函数。
test.py

import module1 as t1
import module2 as t2

t1.foo()
t2.foo()

但是如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个`foo`，因为后导入的foo覆盖了之前导入的`foo`。

test.py

from module1 import foo
from module2 import foo

# 输出goodbye,world!
foo()

test.py
from module2 import foo
from module1 import foo

# 输出hello,world
foo()

需要说明的是，如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非
直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“\_\_main\_\_”。

module3.py

def foo():
    pass
    
def bar():
    pass
    
    
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
    

test.py

import module3

# 导入module3时，不会执行模块中if成立时的代码，因为模块的名字是module3,而不是__main__



# 用模块管理函数：
#     概念：Python模块(Module)，是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。
#          模块让你能够有逻辑地组织你的Python代码段
#          把相关的代码分配到一个模块里能让你的代码更好用，更易懂
#          模块能定义函数，类和变量，模块里也能包含可执行的代码

#     导入模块：1.import语句
#             模块定义好后，我们可以使用import语句来引入模块，语法如下：
#               import module
#             比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时，必须这样引用：模块名.函数名
#               import support       # 导入模块
#               support.print('你好') # 调用模块里包含的函数
#             一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
#             2.from...import语句
#             Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
#               from modname import name
#             比如要导入模块fib的fibonacci函数，使用如下语句：
#               from fib import fibonacci
#             这个声明不会把整个fib模块导入到当前命名空间，只会将fib里的fibonacci单个引入到这个声明的模块的全局符号表
#             可在当前空间直接使用fibonacci，无需加前缀fib.
#             3.from...import * 语句
#             把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#               from modname import *
#             这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

#     使用as给函数指定别名：
#             如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名 别名 ——函数的另一个名称，类似于外号。
#               下面给函数make_pizza() 指定了别名mp() 。这是在import 语句中使用make_pizza as mp 实现的，关键字as 将函数重命名为你提供的别名：
#               from pizza import make_pizza as mp
#              通用语法：
#               from module_name import function_name as fn

#      使用as给模块指定别名：
#              如给模块pizza 指定别名p：
#               import pizza as p
#              上述import 语句给模块pizza指定了别名p，但该模块中所有函数的名称都没变。调用函数make_pizza() 时，
#              编写代码p.make_pizza()而不是pizza.make_pizza()，这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。
#              通用语法：
#               import module_name as mn



# 课后练习题
# # 练习1：实现计算求最大公约数和最小公倍数的函数
# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x,0,-1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
# def lcm(x,y):
#     return x * y // gcd(x, y)
#
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
#
# print(num1,"和",num2,"的最大公约数为",gcd(num1,num2))       # 求最大公约数
# print(num1,"和",num2,"的最大公倍数为",lcm(num1,num2))       # 求最小公倍数


# # 练习2:实现判断一个数是不是回文数的函数
# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#         return total == num
#
#
# # 练习3：实现判断一个数是不是素数的函数。
#
# def is_prime(num):
#     for factor in range(2, num):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False
#
#
#
# # 练习4：写一个程序判断输入的正整数是不是回文素数。
# if __name__ == '__main__':
#     num = int(input('请输入正整数: '))
#     if is_palindrome(num) and is_prime(num):
#         print('%d是回文素数' % num)
#     else:
#         print("该数不是回文素数，请重新再输！")


'''

