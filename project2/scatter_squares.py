# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:45:05 2018

@author: Charlotte
"""

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,edgecolor='none',s=40)

#设置图表标题并给坐标轴加上标签
plt.title("Squre Number",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize =14)
plt.axis([0,1100,0,1100000])

plt.savefig('square_plot.png',bbox_inches ='tight')
