# -*- coding: utf-8 -*-
'''
Created on 2016��4��3��

@author: Zhangzirui(411489774@qq.com)
'''

import numpy as np

class RandCent(object):
    
    def create_cent(self,dataSet, k):
        n = np.shape(dataSet)[1]            #n为矩阵的列数，即为2
        centroids = np.mat(np.zeros((k,n))) #创建装载质心的矩阵
        for j in range(n):  #生成质心
            minJ = min(dataSet[:,j]) 
            rangeJ = float(max(dataSet[:,j]) - minJ)
            centroids[:,j] = np.mat(minJ + rangeJ * np.random.rand(k,1))
        return centroids


    
    

    

    
    


