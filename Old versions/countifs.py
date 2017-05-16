# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:25:54 2017

@author: eardo
"""
import numpy as np
import os as os
import matplotlib.pyplot as plt

indir="/Users/Daniel/Desktop/farmscripts"
os.chdir(indir)
freq=[]
indata= np.genfromtxt('all data_1.csv', delimiter = ',')
x= indata[:,0]*-1
y=(indata[:,1])
y= y[np.logical_not(np.isnan(y))]

xedges= np.linspace(6, 30, 100)
yedges  = np.logspace(-2, 2, 100 )



H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))

sum1=np.sum(H)

im = plt.imshow(H, interpolation='nearest', origin='low',
                extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])


'''


#data1=np.genfromtxt('freqtable.csv',  delimiter=',')
#x,y=np.meshgrid(binx,biny)

Tz=np.round(indata[:,0],2)
Tz= Tz[np.logical_not(np.isnan(Tz))]
INPz=indata[:,1]

for i in range(len(Tz)):
    for j in range(len(binx)):
        if (j < len(binx)-1):
            if (binx[j] < Tz[i]) & (Tz[i] < binx[j+1]): 
                np.round(Tz[i],2)
                a=Tz[i]
                format(a, '.2f')
                for j in range(len(Tz)):
                    if a:
                        print(indata[i:1])
                    #print indata[i:1]

        #if (biny[0,j] < INPz) & (INPz < biny[0,j+1]):
        

for i in range(0,len(x)):
    for j in range (0, len(y)):
        if (i < len(x)-1 and j <len(y)-1):
        
            a =  (y[0,j] < INPz) & (INPz < y[0,j+1]).sum()  #step accross columns
            print i
            freq.append(a)
'''        
#for j in range(0,len(biny)):
 #   if j < len(biny)-1:
        
  #      b = ((biny[i] < INPz) & (INPz < biny[i+1])).sum()
        
   #     freq.append(a)'''
