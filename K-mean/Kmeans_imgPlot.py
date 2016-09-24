# -*- coding: utf-8 -*-
'''
Created on 2016��4��3��

@author: Zhangzirui(411489774@qq.com)
'''
import matplotlib.pyplot as plt

class ImgPlot(object):
    
    def show(self,centroids,k,dataSet,clusterAssment):

        dataRows = dataSet.shape[0]
        
#         mark1 = ['or','^g','sb','>k','<y']
        for i in range(dataRows):
            markIndex = int(clusterAssment[i,0])
            plt.plot(dataSet[i,0],dataSet[i,1],'ob')
#             plt.plot(dataSet[i,0],dataSet[i,1],mark1[markIndex])
        
        mark2 = ['xr','xg','xb','xk','xy']
        for i in range(k):
            plt.plot(centroids[i,0],centroids[i,1],mark2[i],markersize=15);
        
        plt.show()    


