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





'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

import numpy as np
import os as os
import matplotlib.pyplot as plt








indir=('/Users/Daniel/Desktop/farmscripts/')
os.chdir(indir)

'''DMT_T=np.genfromtxt('demott.csv', delimiter = ',')[:,0]
DMT_I=np.genfromtxt('demott.csv', delimiter = ',')[:,1]
DMT_T= DMT_T[np.logical_not(np.isnan(DMT_T))]
DMT_I=DMT_I[np.logical_not(np.isnan(DMT_I))]


pettersup=np.genfromtxt('pettersup.csv', delimiter = ',')
pupT=pettersup[:,0]
pupT= pupT[np.logical_not(np.isnan(pupT))]

pupINP=pettersup[:,1]
pupINP= pupINP[np.logical_not(np.isnan(pupINP))]


pettersdown= np.genfromtxt('pettersdown.csv', delimiter = ',')
pdownT=pettersup[:,0]
pdownT= pupT[np.logical_not(np.isnan(pupT))]

pdownINP=pettersdown[:,1]
pdownINP= pdownINP[np.logical_not(np.isnan(pupINP))]'''


indata= np.genfromtxt('iced_compiled.csv', delimiter = ',', usecols = (1,2), skip_header =1)
inx= indata[:,0]*-1
iny=(indata[:,1])


xedges= np.linspace(5, 32, 50)
yedges  = np.logspace(-1, 7.3, 50)



H, xedges, yedges = np.histogram2d(inx, iny, bins=(xedges, yedges))


sum1=np.sum(H)
H=H/sum1*100
z=np.transpose(H)
degree_sign= u'\N{DEGREE SIGN}'





T=inx
INP=iny
x,y=np.meshgrid(xedges[0:-1]*-1,yedges[0:-1])


#Smoothing step
#z = ndimage.gaussian_filter(z, sigma=0.2, order=0)
data2= np.genfromtxt('iced_compiled.csv', delimiter = ',', usecols = (1,2), skip_header =1)
#Change Figure size
fig=plt.figure(figsize= (8,4))

#set levels for contour plot

levels = np.linspace(0.1, 2.027, 50)

##################################################
#Setup fig
ax1 = fig.add_subplot(1,2,2, axisbg='white')
ax2 = fig.add_subplot(121)
#p1=ax1.contourf(x,y,z)

p1=ax1.contourf(x,y,z, levels = levels, extend = 'both')
#ax1.plot(pupT, pupINP)
#ax1.plot(pdownT, pdownINP)


cmap = plt.get_cmap()
cmap.set_under('black')


#p1.set_clim(0, 1)
cbaxes=fig.add_axes([1, 0.1, 0.02, 0.8]) 
cb = fig.colorbar(p1, cax = cbaxes, label='% of Total Observations', format ='%0.2f')


    



p2=ax2.plot(data2[:,0],data2[:,1], linewidth=0,marker="o", zorder =0 )

#ax2.scatter(DMT_T,DMT_I, marker="x", color = "red")

#################
#ax1 properties
ax1.set_yscale('log')
ax1.set_xlim(-30,-5)
ax1.set_ylim(10,10000000)
ax1.set_xlabel('T ('+degree_sign+'C)')
ax1.set_ylabel('[INP] $m^-3$')
ax1.get_yaxis().set_tick_params(which='both', direction='out')
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.set_title("Frequency of Occurence", fontsize=14)
ttl1 = ax1.title
ttl1.set_position([.5, 1.05])



######################
#ax2 properties


ax2.set_yscale('log')
ax2.set_xlim(-30,-5)
ax2.set_ylim(10,10000000)
ax2.get_yaxis().set_tick_params(which='both', direction='out')
ax2.get_xaxis().set_tick_params(which='both', direction='out')
ax2.set_xlabel('T ('+degree_sign+'C)')
ax2.set_ylabel('[INP] $m^-3$')
ax2.set_title("Original Data", fontsize=14)
ttl2 = ax2.title
ttl2.set_position([.5, 1.05])

#####################
#==============================================================================
# otherdata = "/Users/eardo/Desktop/Farmscripts/Past Data"
# os.chdir(otherdata)
# pastdata=np.genfromtxt('Past Data.csv', skip_header=0, delimiter =",")
# Garcia = pastdata[1:,0:2]
# Belosi = pastdata[1:,2:4]
# ax2.scatter(Belosi[:,0],Belosi[:,1], marker="x", color = "red")
# ax2.scatter(Garcia[:,0], Garcia[:,1], marker="x", color = "green")
#==============================================================================

plt.tight_layout()
plt.tight_layout()

fig.savefig('contour.png', dpi=100)
plt.show()
