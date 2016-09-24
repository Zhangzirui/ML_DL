# -*- coding: utf-8 -*-
'''
Created on 2016年5月21日

@author: Zhangzirui(411489774@qq.com)
'''
from numpy import *
from time import time

class Batch_gradient_descent(object):
    

    def batch(self,x_arr,y_arr):
        
        #MINI_ERROR表示系统允许最小误差
        MINI_ERROR = 0.00001 
        #alpha表示学习速率
        alpha = 0.001
        #j_theta用来装载最后的损失
        j_theta = 0
        
        theta0 = 1
        theta1 = 1

        theta0_last = 0
        theta1_last = 0
        
        #num用来装载迭代的次数
        num = 0
        m = len(x_arr)
        startTime = time()
        while True:
            num = num + 1
            j_diff = [0,0]
                         
            theta0_last = theta0
            theta1_last = theta1

            for i in range(m):            
                j_diff[0] += (y_arr[i][0] - theta0 -theta1*x_arr[i][0]) 
                j_diff[1] += (y_arr[i][0] - theta0 -theta1*x_arr[i][0]) * x_arr[i][0]
                          
                theta0 = theta0 + alpha * j_diff[0]
                theta1 = theta1 + alpha * j_diff[1]

            if abs(theta0-theta0_last)<MINI_ERROR and abs(theta1-theta1_last)<MINI_ERROR:
                 
                for j in range(m):
                    j_theta += (theta0 + theta1*x_arr[j][0] - y_arr[j][0])**2*(0.5/m) 
                break
            
        endTime = time()
        print "time cost:", endTime-startTime
        print "the times of iteration is %d." % num
        print 'Done: theta0 : %f, theta1 : %f,j_theta: %f.' % (theta0,theta1,j_theta)     
        
    def loadData(self,fileName):
        arr = []
        fr = open(fileName)
        for line in fr.readlines():
            curline = line.strip().split(" ")            
            curline = map(float,curline)
            arr.append(curline)
        return arr    
    
if __name__ == "__main__":
    
    bat = Batch_gradient_descent()
    fileName1 =  "F:\\ML\\stanford\\exercise data\\ex2Data\\ex2x.dat"
    fileName2 =  "F:\\ML\\stanford\\exercise data\\ex2Data\\ex2y.dat"
    x_arr = bat.loadData(fileName1)
    y_arr = bat.loadData(fileName2)  
    bat.batch(x_arr, y_arr)   