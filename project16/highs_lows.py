# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:03:39 2018

@author: Charlotte
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt

#从文件中获取最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)    #生成阅读器
    header_row = next(reader) #函数next(),输入阅读器对象，返回文件下一行
    
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high =int(row[1])
            low = int(row[3])
            
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
#根据数据描绘图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c='red',alpha=0.5)#alpha是指颜色透明度，0表示透明
plt.plot(dates,lows, c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制斜的日期标签，以免重叠
plt.ylabel("Temperature(F)",fontsize= 16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

    