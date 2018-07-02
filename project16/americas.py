# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:11:47 2018

@author: Charlotte
"""
import pygal

wm = pygal.maps.world.World()

wm.title = 'North, Central, and South America'

wm.add('North America',['ca','mx','us'])

wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])

wm.add('South America',['ar','bo','br','cl','co','ec','gf',
                        'gy','pe','py','sr','uy','ve'])

wm.render_to_file('E:/programme_data/project16/americas.svg')
