# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:21 2017

@author: eardo
"""

import numpy as np
import os as os
import glob as glob
import csv
import matplotlib.pyplot as plt

infolder = 'W:\\161027\\SMPS\\'
os.chdir(infolder)
x=glob.glob('*.csv')


#####################################################################
data=[]
with open(x[0]) as csvfile:
    reader = csv.reader(csvfile, delimiter =',')
    data=[row for row in reader]
    
header = data[25]

size= np.array(header[9:], dtype = float)
size=(size)/1000
for i in range(len(x)):
        indata= np.genfromtxt(x[i], delimiter =',', skip_header=26)[:,9:]
    
SMPSavnum=np.mean(indata, axis = 0)

for i in range(len(size))
    bins[i]=size[i]
fig = plt.figure() 
ax1=plt.scatter(size, SMPSavnum)
plt.xscale('log')
plt.yscale('log')

######################################################################

infolder = 'W:\\161027\\APS\\'
os.chdir(infolder)
x=glob.glob('*.csv')


with open(x[0]) as csvfile:
    reader = csv.reader(csvfile, delimiter =',')
    APSdata=[row for row in reader]
    
APSheader = APSdata[6]

APSsize= (APSheader[5:54])
APSsize = [float(i) for i in APSsize]


for i in range(len(x)):
        APSdata= np.genfromtxt(x[i], delimiter =',', skip_header=7)[:,5:54]

APSdata[APSdata == 0] = np.nan  

APSavnum=np.mean(APSdata, axis = 0) 
plt.xlim(0.01, 20)
ax2 = plt.scatter(APSsize, APSavnum, c = 'red')
plt.ylim(0.01,100)
plt.xscale('log')
plt.yscale('log')



