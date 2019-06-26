'''
# 1、用python实现------华氏温度转换为摄氏温度

  # 输入华摄氏度
  fahrenheit = float(input('输入华氏度:'))
  celsius = (fahrenheit - 32) / 1.8 
  # 计算摄氏度
  print('%.1f华氏度转为摄氏度为%.1f' % (fahrenheit, celsius))
  
  
# 2、输入圆的半径计算周长和面积
  
  import math
  r=float(input("请输入半径："))
  circumference = 2*math.pi*r
  area=math.pi*r*r

  print ( "圆的周长: %.2f" % circumference)
  print ( "圆的面积: %.2f"% area)
  
  
# 3、输入年份判断是否是闰年
  # -*- coding: UTF-8 -*-
 year=int(input("输入一个年份："))
 if year % 100 == 0:
    if year % 400 == 0:
        print('%d年是闰年' %year)
    else:
        print('%d年不是闰年' %year)
 else:
    if year%4==0:
        print('%d年是闰年' %year)
    else:
        print('%d年不是闰年' %year)









'''
