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
    print('hello worl的！')

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


'''

