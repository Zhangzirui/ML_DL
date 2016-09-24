# -*- coding: utf-8 -*-
'''
Created on 2016年5月9日

@author: Zhangzirui(411489774@qq.com)
'''
from numpy import * 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class LinearRegression(object):
    
    
    def loadData(self,fileName):
        dataset = []
        fr = open(fileName)
        for line in fr.readlines():
            curLine = line.strip()
            fltLine = float(curLine)
            dataset.append(fltLine)
        return transpose(mat(dataset))
    
    def l_r(self,f1,f2):
        
        x = self.loadData(f1)
        y = self.loadData(f2)
        
        plt.figure("fig1")
        plt.plot(x,y,'ob')
        plt.xlabel("height")
        plt.ylabel("years")
         
        m = len(y)
        x1 = ones((m,2))
        
        for i in range(m):
            x1[i,1] = x[i,0]
            
        theta = zeros((2,1))
        alpha = 0.07
        MAX_IIR = 1500  #theta最大的迭代次数
        ERROR = 1e-10   #允许的误差
        
        

        for i in range(MAX_IIR):
            grad = dot(1.0/m*transpose(x1),dot(x1,theta)-y)  #损失函数 = X'*X*theta - X'*Y 
            prev_theta = theta
            theta = theta - alpha*grad
            if [j for j in abs(prev_theta - theta) if j<ERROR] == abs(prev_theta - theta):
                break
 
        plt.plot(x,dot(x1,theta),label='linear regression')
        
        
        # 为了更好理解batch梯度下降所做的事情，这里画出J(theta)也就是损失与theta之间的关系
        j_vals = zeros((100,100))
        theta0_vals = linspace(-3,3,100)
        theta1_vals = linspace(-1,1,100)
        

        for i in range(len(theta0_vals)):
            for j in range(len(theta1_vals)):
                t = array([[theta0_vals[i]],[theta1_vals[j]]])
                j_vals[i,j] = 0.5/m*sum([val**2 for val in dot(x1,t)-y])   
        

        fig2 = plt.figure("fig2")
        ax = Axes3D(fig2)
        ax.plot_surface(theta0_vals,theta1_vals,j_vals,rstride=5,cstride=5,cmap='hot')
        ax.set_xlabel('theta0')
        ax.set_ylabel('theta1')
        ax.set_zlabel('j(theta)')

        plt.legend() #显示label的图示
        plt.show()


if __name__ == "__main__":
    
    f1 = "F:\ML\stanford\exercise data\ex2Data\ex2x.dat"
    f2 = "F:\ML\stanford\exercise data\ex2Data\ex2y.dat"
    m = LinearRegression()
    m.l_r(f1, f2)
    