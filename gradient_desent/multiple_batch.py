# -*- coding: utf-8 -*-
'''
Created on 2016年5月21日

@author: Zhangzirui(411489774@qq.com)
'''

from numpy import *
import matplotlib.pyplot as plt

class Multiple_batch(object):
    
    def batch(self,x_arr,y_arr):  
        
        #最大迭代次数
        MAX_ITERATION = 50
        #alpha表示学习速率
        alpha = [0.001,0.01]
        #用来装载最后的误差损失
        j_all = []
        
        
#         theta0_last = 0
#         theta1_last = 0
#         theta2_last = 0
        
        m = len(x_arr)
        
        #分别用不同收敛速度alpha
        for a in alpha:
            
            theta0 = 1
            theta1 = 1
            theta2 = 1
            #num表示迭代的次数
            num = 0
            j_thetas = []
            while num<MAX_ITERATION:
                
                num = num + 1
                j_theta = 0
                
                #计算每次迭代后的损失函数大小
                for j in range(m):
                    j_theta += (theta0 + theta1*x_arr[j][0] + theta2*x_arr[j][1] - y_arr[j][0])**2*(0.5/m) 
                j_thetas.append(j_theta)

                j_diff = [0,0,0]
                for i in range(m):            
                    j_diff[0] += (y_arr[i][0] - theta0 -theta1*x_arr[i][0] - theta2*x_arr[i][1]) 
                    j_diff[1] += (y_arr[i][0] - theta0 -theta1*x_arr[i][0] - theta2*x_arr[i][1]) * x_arr[i][0]
                    j_diff[2] += (y_arr[i][0] - theta0 -theta1*x_arr[i][0] - theta2*x_arr[i][1]) * x_arr[i][1]
#                 
#                 theta0_last = theta0
#                 theta1_last = theta1
#                 theta2_last = theta2
                
                theta0 = theta0 + a * j_diff[0]
                theta1 = theta1 + a * j_diff[1]
                theta2 = theta2 + a * j_diff[2]          
                
#                 if abs(theta0-theta0_last)<MINI_ERROR and abs(theta1-theta1_last)<MINI_ERROR and abs(theta2-theta2_last)<MINI_ERROR:
#                     print "jump",num
#                     for j in range(m):
#                         j_theta += (theta0 + theta1*x_arr[j][0] + theta2*x_arr[j][1] - y_arr[j][0])**2*(0.5/m) 
#                     break
#                 print a
#                 print num
                
            j_all.append(j_thetas)        

        mark = ['-r','-g']
        x = arange(0,MAX_ITERATION,1)
        for i in range(len(mark)):
            plt.plot(x,j_all[i],mark[i],linewidth=3)
        plt.xlabel(u"迭代次数num",fontproperties='SimHei')
        plt.ylabel(u"损失函数j_theta",fontproperties='SimHei')
        plt.show()
        
    def loadData(self,fileName):
        arr = []
        fr = open(fileName)
        for line in fr.readlines():
            curline = line.strip().split("   ")
            curline = map(float,curline)
            arr.append(curline)
        return arr    
    
if __name__ == "__main__":
    
    bat = Multiple_batch()
    fileName1 =  "F:\\ML\\stanford\\exercise data\\ex3Data\\ex3x.dat"
    fileName2 =  "F:\\ML\\stanford\\exercise data\\ex3Data\\ex3y.dat"
    x_arr = bat.loadData(fileName1)

    #数据预处理
    x_arr = (x_arr - mean(x_arr, axis=0))/std(x_arr,axis=0)
    
    y_arr = bat.loadData(fileName2)  
    bat.batch(x_arr, y_arr)   