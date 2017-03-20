# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 12:10:42 2017

@author: eardo
"""
import matplotlib.pyplot as plt
import numpy as np
import os as os
import scipy.ndimage as ndimage
from matplotlib.gridspec import GridSpec


indir="U:\pyoutput\Frequency analysis"
os.chdir(indir)


'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

degree_sign= u'\N{DEGREE SIGN}'
data1=np.genfromtxt('freqtable.csv',  delimiter=',')
T=data1[1:,0]
logINP=data1[0,1:]
INP=logINP
x,y=np.meshgrid(T,INP)
freqs=np.genfromtxt('freqtable.csv',  delimiter=',')
z=data1[1:,1:]
z=np.transpose(z)

#Smoothing step
z = ndimage.gaussian_filter(z, sigma=1, order=0)
data2=np.genfromtxt('all data.csv',  delimiter=',')
#Change Figure size
fig=plt.figure(figsize= (8,4))

#set levels for contour plot
levels = np.linspace(0.001, 0.55, 9)
##################################################
#Setup fig
ax1 = fig.add_subplot(1,2,2, axisbg='black')
ax2 = fig.add_subplot(121)
#p1=ax1.contourf(x,y,z)
p1=ax1.contourf(x,y,z, levels = levels, extend ="both")


cmap = plt.get_cmap()
cmap.set_under('k')


#p1.set_clim(0, 1)
cbaxes=fig.add_axes([1, 0.1, 0.02, 0.8]) 
cb = fig.colorbar(p1, cax = cbaxes, label='% of Total Observations')





p2=ax2.plot(data2[:,0],data2[:,1], linewidth=0,marker="o" )


#################
#ax1 properties
ax1.set_yscale('log')
ax1.set_xlim(-28,-5)
ax1.set_ylim(0.01,100)
ax1.set_xlabel('T ('+degree_sign+'C)')
ax1.set_ylabel('[INP] /L')
ax1.get_yaxis().set_tick_params(which='both', direction='out')
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.set_title("Frequency of Occurence", fontsize=14)
ttl1 = ax1.title
ttl1.set_position([.5, 1.05])



######################
#ax2 properties


ax2.set_yscale('log')
ax2.set_xlim(-28,-5)
ax2.set_ylim(0.01,100)
ax2.get_yaxis().set_tick_params(which='both', direction='out')
ax2.get_xaxis().set_tick_params(which='both', direction='out')
ax2.set_xlabel('T ('+degree_sign+'C)')
ax2.set_ylabel('[INP] /L')
ax2.set_title("Original Data", fontsize=14)
ttl2 = ax2.title
ttl2.set_position([.5, 1.05])

#####################


plt.tight_layout()
plt.tight_layout()

fig.savefig('contour.png', dpi=100)
plt.show()