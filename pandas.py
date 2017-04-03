# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 12:28:00 2017

@author: eardo
"""
import os as os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

infolder = 'C:\Users\eardo\Desktop\Farmscripts\glomap data'
os.chdir(infolder)

df1 = pd.read_csv('INP_variability_marine_Farm.csv', index_col = 0)
df1.columns = ['-15m', '-20m', '-25m']

df2 = pd.read_csv('INP_variability_feldspar_Farm.csv', index_col = 0)
df2.columns = ['-15f', '-20f', '-25f']

alldata = pd.concat([df1,df2], axis =1)

alldata.index.rename('Days', inplace = True)


#ax1=alldata.reset_index().plot.scatter( x= 'Days', y = '-15m')
#ax2=alldata.reset_index().plot.scatter( x= 'Days', y = '-20m')
#ax1.yscale('log')
plt.scatter(alldata.index, alldata['-15m'],color='b')
plt.scatter(alldata.index, alldata['-20m'],color='r')

