# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 10:52:24 2017

@author: eardo
"""
import os as os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
degree_sign= u'\N{DEGREE SIGN}'


infolder = "C:\Users\eardo\Desktop\Farmscripts\MetData"
os.chdir(infolder)
data15=pd.read_excel("15corr.xlsx", header = 0)
data20=pd.read_excel("20corr.xlsx", header = 0)
data25=pd.read_excel("corr25.xlsx", header = 0)
corr15=data15.corr(method = 'pearson')
corr20=data20.corr(method = 'pearson')
corr25=data25.corr(method = 'pearson')


ax= plt.subplot(111)


x = corr15.loc['Time':'Mean Wind Speed',['LogINP']].values
y = corr20.loc['Time':'Mean Wind Speed',['LogINP']].values
z = corr25.loc['Time':'Mean Wind Speed',['LogINP']].values
index = corr15.index
index = index[1:12]
y_pos = np.arange(len(index))
ax.bar(y_pos-0.2, x, align = 'center', width=0.2, color = 'b')
ax.bar(y_pos, y, align = 'center',width=0.2, color = 'r')
ax.bar(y_pos+0.2, z, align = 'center',width=0.2, color = 'g')
plt.xticks(y_pos,index, rotation = 'vertical')
plt.xlim(-0.5,10.5)
plt.ylim(-1,1)


#==============================================================================
# ax.bar(corr15.loc['Time':'Mean Wind Speed',['LogINP']],corr15.loc['Time':'Mean Wind Speed',['LogINP']],color = 'red')
# plt.ylim(-1,1)
# plt.ylabel('Pearson R Coefficient')
# plt.title('T= -15'+degree_sign+'C')
# corr20.loc['Time':'Mean Wind Speed',['LogINP']].plot(kind = 'bar', color = 'blue')
# plt.ylim(-1,1)
# plt.ylabel('Pearson R Coefficient')
# plt.title('T= -20'+degree_sign+'C')
# corr25.loc['Time':'Mean Wind Speed',['LogINP']].plot(kind = 'bar',color = 'green')
# plt.ylim(-1,1)
# plt.ylabel('Pearson R Coefficient')
# plt.title('T= -25'+degree_sign+'C')
#==============================================================================
