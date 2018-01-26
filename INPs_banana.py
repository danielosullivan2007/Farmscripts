# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:31:25 2018

@author: eardo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs
import datetime
from myfuncs import jd_to_date, degree_sign
import time
import math
import matplotlib.ticker
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter, MaxNLocator, LogLocator, LogFormatterExponent,FormatStrFormatter,LogFormatterMathtext 
from matplotlib.colors import LogNorm
import time
import matplotlib.gridspec as gridspec
from matplotlib.ticker import StrMethodFormatter, NullFormatter
import itertools



label=[]
xlabel =[]
cbar_labs=[]
dt=[]
dt_label=[]
hours =[]
q=[]
mask=[]

inps  = pd.read_pickle(farmdirs['pickels']+'binned_INPs_witherrors_timestamps.p')
inps.reset_index(drop=True, inplace=True)
inps['start']= pd.to_datetime(inps['start'])
inps['end']= pd.to_datetime(inps['end'])


inps['julian_start'] = [inps['start'][i].to_julian_date() for i in range(len(inps.start))]
inps['julian_end'] = [inps['end'][i].to_julian_date() for i in range(len(inps.end))]

min_T = -26
max_T = -15
step=1


range_T=range(min_T,max_T, step)
len_T=len(range_T)
colors = iter(cm.jet(np.linspace(0, 1, len_T)))
Z = [[0,0],[0,0]]
levels = range(min_T,max_T+step,step)
CS3 = plt.contourf(Z, levels, cmap= 'jet')
plt.clf()


fig, ax = plt.subplots(figsize=(5,3))


for i in range(min_T, max_T, step):
    
    subset_T = inps[inps['T']==i]
    ax.scatter(subset_T['julian_start'], subset_T['INP'], color = next(colors))


ax.set_yscale('log')



#FORMAT X AND Y TICK LABELS
plt.xlim(2457655, 2457690.1666666665)

ticks = ax.get_xticklabels()
plt.draw()
#NEXT STEPS CHANGE JULIAN FORMATTING TO DATETIME
q = [item.get_text() for item in ax.get_xticklabels()]
[xlabel.append('') if q[i]=='' else xlabel.append(float(q[i])+2.45765e6)for i in range(len(q))]
[dt.append('') if q[i]=='' else dt.append(list(jd_to_date(xlabel[i])))for i in range(len(xlabel))]
for i in range(len(dt)):
    if dt[i]=='':
        hours.append('')
    else:
        hours.append(dt[i][2]%1*24)
        dt[i].append(int(hours[i]))
        dt[i][2]=int(math.floor(dt[i][2]))
        dt[i]=tuple(dt[i])
        dt[i]=datetime.datetime(*dt[i])
        dt[i]=datetime.datetime.strftime( dt[i].date(), '%d/%m')
ax.set_xticklabels(dt)
#ax.tick_params(labelbottom='off')


plt.ylabel('INPs ($L^{-1}$)', fontsize =8)
plt.xlabel('Date')



cbaxes=fig.add_axes([0.95, 0.22, 0.02, 0.6]) 
cb = fig.colorbar(CS3, cax = cbaxes)
cb.ax.invert_yaxis()
cb.ax.set_title('T ('+degree_sign+'C)', fontsize =8)

