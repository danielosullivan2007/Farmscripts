# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 12:10:42 2017

@author: eardo
"""
import matplotlib.pyplot as plt
import numpy as np
import os as os

from matplotlib.gridspec import GridSpec


indir="U:\pyoutput\Frequency analysis"
os.chdir(indir)


'''DATA MUST BE IN LOG BINS BY INP NUMBER'''

degree_sign= u'\N{DEGREE SIGN}'
data1=np.genfromtxt('freqtable.csv',  delimiter=',')
T=data1[1:,0]
logINP=data1[0,1:]
INP=10**logINP
x,y=np.meshgrid(T,INP)
freqs=np.genfromtxt('freqtable.csv',  delimiter=',')
z=data1[1:,1:]
z=np.transpose(z)
data2=np.genfromtxt('all data.csv',  delimiter=',')
fig=plt.figure()



ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
p1=ax1.contourf(x,y,z,)
cmap = plt.get_cmap()
cmap.set_under(color='black')
cbaxes=fig.add_axes([1, 0.55, 0.02, 0.4]) 
cb = fig.colorbar(p1, cax = cbaxes, label='% of Total Observations')





p2=ax2.plot(data2[:,0],data2[:,1], linewidth=0,marker="o" )





ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xlim(-28,-5)
ax2.set_xlim(-28,-5)

ax1.set_ylim(0.05,60)
ax2.set_ylim(0.05,60)

ax1.set_xlabel('T ('+degree_sign+'C)')
ax1.set_ylabel('[INP] /L')
ax1.get_yaxis().set_tick_params(which='both', direction='out')
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.set_title("Frequency of Occurence")
ax2.get_yaxis().set_tick_params(which='both', direction='out')
ax2.get_xaxis().set_tick_params(which='both', direction='out')
ax2.set_xlabel('T ('+degree_sign+'C)')
ax2.set_ylabel('[INP] /L')
ax2.set_title("Original Data")
plt.tight_layout()

fig.savefig('test2png.png', dpi=100)
plt.show()