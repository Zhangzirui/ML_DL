# -*- coding: utf-8 -*-
'''
Created on 2016��4��3��

@author: Zhangzirui(411489774@qq.com)
'''

from numpy import * 

class CountDistance(object):
    
    def count_distance(self,vecA, vecB):      #距离计算函数
        return sqrt(sum(power(vecA - vecB, 2))) 


