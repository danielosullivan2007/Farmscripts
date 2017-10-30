# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:33:10 2017

@author: eardo
"""

from directories import farmdirs, bardirs
import pandas as pd
import matplotlib.pyplot as plt


degree_sign= u'\N{DEGREE SIGN}'
bar=pd.read_csv(bardirs['pickels']+'regular_run_INPs.csv')
farm = pd.read_csv(farmdirs['pickels']+'INPs_trim_witherrs.csv')
farm_heat = pd.read_csv(farmdirs['pickels']+'heat_INPs_trim_witherrs.csv')
iced= pd.read_csv(farmdirs['iced']+'iced_compiled.csv')

fig, ax = plt.subplots()
ax1= plt.scatter(bar['Temp'], bar['INP'], color ='orange',
                 edgecolors = 'black', zorder =20, label ='Barbados \'17')
ax2=plt.scatter(farm['T'], farm['INPs_perL'], color ='green',
                edgecolors = 'black',  label ='UK \'16')
#ax3=plt.scatter(farm_heat['T'], farm_heat['INPs_perL'], color ='red')
#ax4=plt.scatter(iced['T'], iced['inp_air']/1000, color ='b',
                #edgecolors = 'black', label = 'Cape Verde \'15', alpha=0.8)
plt.yscale('log')
plt.ylim(0.001, 5000)
plt.xlim(-30, -5)
plt.legend()

plt.ylabel('[INPs] ($\mathregular{L^{-1}}$)')
plt.xlabel('T ('+degree_sign+'C)')
plt.grid()

plt.savefig(bardirs['figures']+'comparison_to_others')



























del  farmdirs, bardirs