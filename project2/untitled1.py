# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:48:30 2018

@author: Charlotte
"""


"""n种商品 m种优惠满减
    ai价格 1表示可八折优惠0表示不可以
    满bi减ci
    
    求和比较：全部为1的八折求和
            总价求和选减最多的求和
"""
import sys

products = []
coupons = []
new_product={}
new_coupon={}
sum1 = 0
sum2 = 0
 
n , m = input().split()
    #录入n个商品信息
for i in range(int(n)):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    new_product['price'],new_product['discount'] = map(int, line.split())
    products.append(new_product)
    sum1 += new_product['price'] #不打折总价
    sum2 += float(new_product['price'] * new_product['discount'])
    
sum2 = sum1 - sum2*0.2  #打八折总价
sum3 = sum1

 #录入n个满减信息
for j in range(int(m)):
    coupon = input().split()
    new_coupon['full'] =int(coupon[0])
    new_coupon['reduction'] =int(coupon[1])
    if sum1 >= new_coupon['full'] and sum3 >= sum1-new_coupon['reduction']:
        sum3 = sum1-new_coupon['reduction']
    
if sum2 > sum3:
    print ("%.2f" % sum3)
else:
    print("%.2f" % sum2)