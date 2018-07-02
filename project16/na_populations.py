# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:27:18 2018

@author: Charlotte
"""

import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America',{'ca':34126000,'us':309349000,'mx':113423000})

wm.render_to_file('E:/programme_data/project16/na_populations.svg')