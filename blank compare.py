# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:11:00 2017

@author: eardo
"""

from datetime import datetime
import os, os.path
from glob import glob
import numpy as np
from os import listdir

import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import matplotlib.patches as mpatches
import socket
from directories import farmdirs
from myfuncs import degree_sign


blanks = pd.read_csv(farmdirs['pickels']+'blanks.csv')
blanks.rename(columns = {'# temperatures':'temp'}, inplace =True)
data = pd.read_csv(farmdirs['pickels']+'MFC2_MFC3.csv')
hepas =  pd.read_csv(farmdirs['pickels']+'hepas.csv')
hepas =hepas[hepas['sample']!='a']


#blanks['date']=pd.to_datetime(blanks['date'])


fig, ax =plt.subplots(figsize =(5,5))
ax.scatter(blanks['temp'], blanks['K'], color='r', alpha =0.3, label = 'MilliQ water')
ax.scatter(hepas['temp'], hepas['K'], color ='b', label ='Hepa filter on inlet')
ax.scatter(data['T'], data['K'], color ='k', alpha =0.7)
ax.set_yscale('log')
ax.set_ylim(10, 10000)
ax.set_xlabel('T ('+degree_sign+'C)')
ax.set_ylabel('INPs (/mL water)', fontsize =8)
plt.legend(scatterpoints=1, fontsize =8)

dates = data['run_date'].unique()

n=0
for i in range(len(dates)):
    n+=1
    plot1= data[data['run_date'] == dates[i]]
    plot2= blanks[blanks['date'] == dates[i]]
    
    print dates[i]
    fig, ax1 = plt.subplots(figsize =(2.5,2.5))
    ax1.set_yscale('log')
    ax1.set_ylim(100, 10000)
    ax1.set_xlim(-35, -5)
    #ax1.set_yscale('log')
    ax1.scatter(plot1['T'], plot1['K'], label = dates[i])
    ax1.scatter(plot2['temp'], plot2['K'], color = 'red', label = dates[i])
    ax1.legend(fontsize=8, scatterpoints =1)
    
    
    
    


