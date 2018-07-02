# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:51:59 2018

@author: Charlotte
"""

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到指定的国家，就返回none
    return None
