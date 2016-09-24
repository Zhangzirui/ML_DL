# -*- coding: utf-8 -*-
'''
Created on 2016年4月3日

@author: Zhangzirui(411489774@qq.com)
'''
# Box plots with custom fill colors

import matplotlib.pyplot as plt
import numpy as np


class BoxPlot(object):
    
    def box_plot(self,all_data):

        axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))[1]

        # rectangular box plot
        bplot = axes.boxplot(all_data,
                            vert=True,   # vertical box aligmnent
                            patch_artist=True)   # fill with color
        
        
        # fill with colors
        colors = ['pink', 'lightblue', 'lightgreen']

        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        
        # adding horizontal grid lines
        axes.yaxis.grid(True)
        axes.set_xlabel('xlabel')
        axes.set_ylabel('ylabel')

        
        plt.show()