# -*- coding: utf-8 -*-
'''
Created on 2016��4��3��

@author: Zhangzirui(411489774@qq.com)
'''


class LoadData(object):
    
    def load_dataSet(self,fileName):    #导入数据
        dataMatrix = []                 #创建装载数据的矩阵
        fr = open(fileName)             #打开文件
        for line in fr.readlines():     #读取文件，并装载数据
            curLine = line.strip().split('\t')
            fltLine = map(float,curLine) 
            dataMatrix.append(fltLine)
        return dataMatrix               #返回数据矩阵


