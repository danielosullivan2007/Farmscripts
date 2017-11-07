# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 10:54:13 2017

@author: eardo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs
import matplotlib as mpl
from matplotlib import mlab
from mpl_toolkits.axes_grid1 import make_axes_locatable
import datetime
from myfuncs import jd_to_date
import time
import math
from pylab import show
chi=1.2
rho0=1
rho=2.4

label=[]

dt=[]
dt_label=[]
hours =[]
q=[]

smps=pd.read_pickle(farmdirs['pickels']+'SMPS.p')
aps=pd.read_pickle(farmdirs['pickels']+'APS.p').drop(['Aerodynamic Diameter',
                  'Start Time','Date', '<0.523'], axis =1)

aps.set_index('datetime',drop =True, inplace =True)
smps.set_index('datetimes',drop =True, inplace =True)


aps_diameters = np.array([float(i) for i in list(aps)])
smps_diameters =np.array([float(i) for i in list(smps)])/1000

DpAPS=np.round((((chi*rho0)/rho)**0.5)*aps_diameters,2)
DpSMPS=np.round((1/chi)*smps_diameters,3)


aps.columns = DpAPS
smps.columns  = DpSMPS

del i, aps_diameters

daily_aps  = aps.resample('1d').mean().dropna(axis =0, how ='all')
daily_smps  = smps.resample('1d').mean().dropna(axis =0, how ='all')


merged = daily_aps.join(daily_smps, lsuffix='aps', rsuffix = 'smps')

[label.append('aps') for i in range(len(aps.T))]
[label.append('smps') for i in range(len(smps.T))]




cols=list(merged)
merged = merged.T
merged['type']=label
merged.set_index([label, cols], inplace =True)
merged.index.names = ['type', 'size']
merged.drop('type', axis =1, inplace =True)
merged=merged.T
merged.index = pd.to_datetime(merged.index)
merged = merged.T.sortlevel(level=1).T

merged=daily_aps

#merged=merged['aps']
cols1=list(merged)
#%%
#Plotting section


# =============================================================================
# start = merged.index.min().to_datetime()
# end = merged.index.max().to_datetime()
# delta = datetime.timedelta(hours=1)
# =============================================================================

time1 = [merged.index[i].to_julian_date() for i in range(len(merged.index))]

fig1, ax1 =plt.subplots()
X= time1
Y=cols1
Z = np.log(merged.as_matrix().T)
levels = np.linspace(-3,2.5,1000)
x,y = np.meshgrid(X,Y)
ax1.contourf(x,y,Z, levels=levels,cmap=plt.cm.jet)
ax1.set_yscale('log')
ax1.set_ylim(0.4,1)
ax1.set_facecolor('black')

plt.draw()
#%%
ticks = ax1.get_xticklabels()
q = [item.get_text() for item in ax1.get_xticklabels()]
#q= [ticks[i].get_text() for i in range(len(ticks))]
print q


xlabel =[]
for i in range(len(q)):
    if q[i]=='':
        xlabel.append('')
    else:
        xlabel.append(float(q[i])+2.4576e6)


for i in range(len(xlabel)):
    if xlabel[i]=='':
        dt.append('')
    else:
        dt.append(list(jd_to_date(xlabel[i])))

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
#dt=['','a','b','c','d','e','f','g','']
ax1.set_xticklabels(dt)
#plt.draw()