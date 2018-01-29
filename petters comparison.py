# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:36:29 2017

@author: eardo
"""
import pandas as pd
from directories import farmdirs
import matplotlib.pyplot as plt


degree_sign= u'\N{DEGREE SIGN}'


indata= pd.read_csv(farmdirs['pickels']+'INPs_trim_witherrs.csv')
indata.drop ('Unnamed: 0', inplace =True, axis =1)

past_data=pd.read_csv(farmdirs['lit']+'Past Data.csv')

pettersup = pd.read_csv(farmdirs['lit']+'pettersup.csv')
pettersdown = pd.read_csv(farmdirs['lit']+'pettersdown.csv')

fig, ax=plt.subplots(figsize =(5,5))

ax.scatter(indata['T'], indata.INPs_perL, color ='grey', label = 'This study', alpha =0.7)
ax.scatter(past_data.T1, past_data.Garcia,
           color='forestgreen',edgecolors='darkgreen',
           label = 'Garcia \'12', zorder=19)
ax.scatter(past_data.Bel_feb_T, past_data.Bel_feb_INP,
           color ='r',
           edgecolor='maroon',
           label ='Belosi \'16')
ax.scatter(past_data.Bel_May_T, past_data.Bel_May_INP, 
           color ='r',edgecolor='maroon',
           label ='_nolegend_')
ax.scatter(past_data.Santa_T, past_data.Santa_INP, color ='c',edgecolor='darkblue',
           label ='Santachiari \'10')
ax.plot(pettersup['x'], pettersup['Curve1'], color ='b', linewidth =2, linestyle ='--', label = 'Petters \'16')
ax.plot(pettersdown['x'], pettersdown['Curve1'], color = 'b', linewidth =2, linestyle ='--', label='_nolegend_')

yerr = [past_data.Mason_neg, past_data.Mason_pos]
ax.errorbar(past_data.Mason_T, past_data.Mason_INP, yerr=yerr, 
            color ='k', lw=0, elinewidth=2,capsize=5, capthick =1.5, marker='o',
            markersize =5, markerfacecolor='w',markeredgewidth = 2,  
            label ='Mason \'16', zorder=20)



ax.set_yscale('log')
ax.set_yscale('log')
ax.set_xlabel('T ('+degree_sign+'C)')
ax.set_ylabel('INPs ($\mathregular{L^{-1}}$)')
ax.grid()
plt.xlim(-30, -4)
plt.legend(scatterpoints=1,numpoints =1, loc =3, fontsize = 10)