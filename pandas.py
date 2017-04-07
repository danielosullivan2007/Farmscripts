# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 12:28:00 2017

@author: eardo
"""
import os as os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# infolder = 'C:\Users\eardo\Desktop\Farmscripts\glomap data' #infolder for work
#==============================================================================

degree_sign = u'\N{DEGREE SIGN}'
infolder = '/Users/Daniel/Desktop/farmscripts/glomap data'  #infolder for mac
os.chdir(infolder)

df1 = pd.read_csv('INP_variability_marine_Farm.csv', index_col = 0)
df1.columns = ['-15m', '-20m', '-25m']

df2 = pd.read_csv('INP_variability_feldspar_Farm.csv', index_col = 0)
df2.columns = ['-15f', '-20f', '-25f']

alldata = pd.concat([df1,df2], axis =1)

alldata.index.rename('Days', inplace = True)

alldata['ratio15'] = alldata['-15f']/alldata['-15m']
alldata['ratio20'] = alldata['-20f']/alldata['-20m']
alldata['ratio25'] = alldata['-25f']/alldata['-25m']

fig1 = plt.figure()
plt.scatter(alldata.index, alldata.ratio15, color = 'r')
#plt.scatter(alldata.index, ratio_20, color = 'g')
#plt.scatter(alldata.index, ratio_25, color = 'b')
plt.legend()
plt.yscale('log')
plt.ylim(0.001)
plt.axhline(y=1)
plt.title('ratio of INP sources at -15 '+degree_sign+'C')
plt.xlabel('Day')
plt.ylabel('[INP]$_{Feldspar}$/ [INP]$_{Marine}$$ L^{-1}$')
print 'ratio is less than 1 in '+str(float((alldata['ratio15']<1).sum())/61*100)+'% of cases'


fig1b = plt.figure()
plt.scatter(alldata.index, alldata.ratio20, color = 'r')
#plt.scatter(alldata.index, ratio_20, color = 'g')
#plt.scatter(alldata.index, ratio_25, color = 'b')
plt.legend()
plt.yscale('log')
plt.ylim(0.001)
plt.axhline(y=1)
plt.title('ratio of INP sources at -20 '+degree_sign+'C')
plt.xlabel('Day')
plt.ylabel('[INP]$_{Feldspar}$/ [INP]$_{Marine}$$ L^{-1}$')
print 'ratio is less than 1 in '+str(float((alldata['ratio20']<1).sum())/len(alldata['ratio20']))+'% of cases'


fig1c = plt.figure()
plt.scatter(alldata.index, alldata.ratio25, color = 'r')
#plt.scatter(alldata.index, ratio_20, color = 'g')
#plt.scatter(alldata.index, ratio_25, color = 'b')
plt.legend()
plt.yscale('log')
plt.ylim(0.001)
plt.axhline(y=1)
plt.title('ratio of INP sources at -25 '+degree_sign+'C')
plt.xlabel('Day')
plt.ylabel('[INP]$_{Feldspar}$/ [INP]$_{Marine}$$ L^{-1}$')

#ax1=alldata.reset_index().plot()
#ax2=alldata.reset_index().plot.scatter( x= 'Days', y = '-20m')
#ax1.yscale('log')

#==============================================================================
# fig2=plt.figure(num = 2)
# plt.scatter(alldata.index, alldata['-15m'],color='b')
# plt.scatter(alldata.index, alldata['-20m'],color='r')
# plt.scatter(alldata.index, alldata['-25m'],color='g')
# plt.yscale('log')
#==============================================================================


#==============================================================================
# fig3=plt.figure(num = 3)
# plt.scatter(alldata.index, alldata['-15f'],color='r')
# plt.scatter(alldata.index, alldata['-15m'],color='b')
# plt.legend()
# plt.yscale('log')
# plt.ylim(0.001)
# plt.title('-15C')
#==============================================================================

#==============================================================================
# fig4=plt.figure(num = 4)
# plt.scatter(alldata.index, alldata['-20f'],color='b')
# plt.scatter(alldata.index, alldata['-20m'],color='r')
# plt.yscale('log')
# plt.title('-20C')
#==============================================================================


#==============================================================================
# fig5=plt.figure(num = 5)
# plt.scatter(alldata.index, alldata['-25f'],color='b')
# plt.scatter(alldata.index, alldata['-25m'],color='r')
# plt.yscale('log')
# plt.title('-25C')
#==============================================================================
