# -*- coding: utf-8 -*- 
'''
Created on 2016/3/31


@author: Zhangzirui(411489774@qq.com)
'''
from numpy import *
import math

from K_mean import Kmeans_loadData, Kmeans_countDis, Kmeans_randCent,Kmeans_imgPlot,\
    boxPlot




class K_Means(object):
    
    def __init__(self):
        self.loaddata = Kmeans_loadData.LoadData()
        self.countdis = Kmeans_countDis.CountDistance()
        self.randcent = Kmeans_randCent.RandCent()
        self.imgplot = Kmeans_imgPlot.ImgPlot()
        self.boxplot = boxPlot.BoxPlot()
      
    def kMeans(self,dataSet, k):
        
        m = shape(dataSet)[0]
        clusterAssment = mat(zeros((m,2)))  #创建矩阵，用来承载每个点距离最近质心的索引，及误差
        centroids = self.randcent.create_cent(dataSet, k)  #生成质心矩阵
        
        clusterChanged = True               #是否继续更新质心的判断标准
        while clusterChanged:
            clusterChanged = False
            
            #寻找最近质心
            for i in range(m):  #遍历每一个点
                minDist = inf; minIndex = -1
                for j in range(k):  #遍历每一个质心

                    distJI = self.countdis.count_distance(centroids[j,:],dataSet[i,:])  #计算点与每个质心的距离

                    if distJI < minDist:    #比较距离，得到该点距离最近的质心的索引值，以及最近距离
                        minDist = distJI; minIndex = j            
                if clusterAssment[i,0] != minIndex: clusterChanged = True   #是否所有的点都已经找到了最近的质心
                clusterAssment[i,:] = minIndex,minDist**2 #存储目前每个点所找到质心的索引，及误差

            #更新质心的位置
            for cent in range(k):
                ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#得到对于cent质心周围的点的集合
                centroids[cent,:] = mean(ptsInClust, axis=0) #求均值，axis=none时求全部均值，axis=0求y轴均值，axis=1求x轴均值

        return centroids, clusterAssment
    
    def biKmeans(self,dataSet,k):
     
        #先选出一个质心
        m = shape(dataSet)[0]
        clusterAssment = mat(zeros((m,2)))
        centroid0 = mean(dataSet, axis=0).tolist()[0]   
        centList =[centroid0] 
         
        #存储这个质心造成的误差矩阵
        for j in range(m):
            clusterAssment[j,1] = self.countdis.count_distance(mat(centroid0), dataSet[j,:])**2
             
        while (len(centList) < k):
            lowestSSE = inf
            #将每一个质心进行划分
            for i in range(len(centList)):
                ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]#得到被划分质心的一个集合簇
                centroidMat, splitClustAss = self.kMeans(ptsInCurrCluster, 2)#划分质心
                #算出总误差     总误差 = 被划分的质心造成的误差 + 没被划分的质心造成的误差
                sseSplit = sum(splitClustAss[:,1])#
                sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
#                 print "sseSplit, and notSplit: ",sseSplit,sseNotSplit
                 
                #比较总误差，总误差最小的存储下来
                if (sseSplit + sseNotSplit) < lowestSSE:
                    bestCentToSplit = i     #划分后总误差最小的质心的索引
                    bestNewCents = centroidMat  #质心划分后的两个新的质心
                    bestClustAss = splitClustAss.copy() #生成的两个新质心产生的误差
                    lowestSSE = sseSplit + sseNotSplit  #更新最小误差
     
            bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) #change 1 to 3,4, or whatever
            bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit
     
            #更新质心，将两个新生成的质心替换被划分的质心 （原本质心的簇也划分成两个簇）
            centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]#replace a centroid with two best centroids 
            centList.append(bestNewCents[1,:].tolist()[0])
             
            #将被替换质心的误差换成新的两个质心的误差
            clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss
     
        return mat(centList), clusterAssment 
    
    def run(self,f_name):
        
        dataMatrix = mat(self.loaddata.load_dataSet(f_name))
#      K-mean 聚类
        centList,clusterAssment = self.kMeans(dataMatrix,4)
        centList = self.randcent.create_cent(dataMatrix, 4)
        print centList
        self.imgplot.show(centList, 4, dataMatrix, clusterAssment)
        self.imgplot.show(centList, 4, dataMatrix, clusterAssment)
  
#   画盒图分析        
#         sse = []
#         for k in range(1,11):
#             print k
#             x = 1
#             errorSse = []
#             while x<=50:
#                 clusterAssment = self.kMeans(dataMatrix,k)[1]               
# #                 clusterAssment = self.biKmeans(dataMatrix, k)[1]
#                 errorSse.append(math.log(float(sum(clusterAssment[:,1]))))
#                 x = x + 1
#             sse.append(errorSse)
#         self.boxplot.box_plot(sse)
        
if __name__ == "__main__":
    f_name = "testSet.txt"
    k_m = K_Means()
    k_m.run(f_name)




    
