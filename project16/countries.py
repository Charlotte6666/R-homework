# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:24:34 2018

@author: Charlotte
"""

from pygal.maps.world import COUNTRIES
"""
Whats left of the i18n module can be imported with:

from pygal_maps_world import i18n
"""

for country_code in sorted(COUNTRIES.keys()):#按字母顺序排序
    print(country_code,COUNTRIES[country_code])