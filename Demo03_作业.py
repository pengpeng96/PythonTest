'''
找出100~999之间的所有水仙花数
水仙花数是各立方和等于这个数的本身的数
如：153 = 1**3 + 5**3 + 3**3

'''
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high =num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


# 判断一个数是不是完美数：完全数（Perfect number），又称完美数或完备数，如果一个数恰好等于它的因子之和，则称该数为“完全数”
'''
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
'''
import time
import math

start = time.clock()
for num in range(1,10000):
    sum = 0
    for factor in range(1,int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num /factor != factor:
                sum += num /factor
    if sum == num:
        print(num)
end = time.clock()
print("执行时间：",(end - start),"秒")


'''
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
'''

x = 0
y = 1
for _ in range(20):
    (x, y) = (y, x + y)
    print(x, end=' ')

