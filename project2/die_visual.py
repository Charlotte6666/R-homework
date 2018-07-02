# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:27:17 2018

@author: Charlotte
"""

from die import Die 
import pygal

#创建一个D6
die=Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# added by slc
#print(results)
#分析结果    
frequancies =[]

for value in range(1,die.num_sides+1):
    frequancy = results.count(value)
    frequancies.append(frequancy)
    
# added by slc
print(frequancies)
#对数据进行可视化
hist =pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequancies)
hist.render_to_file('die_visual.svg')
    