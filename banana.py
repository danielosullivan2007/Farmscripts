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

chi=1.2
rho0=1
rho=2.4

label=[]
dt=[]
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
merged=merged['aps']
cols1=list(merged)
#%%
#Plotting section


# =============================================================================
# start = merged.index.min().to_datetime()
# end = merged.index.max().to_datetime()
# delta = datetime.timedelta(hours=1)
# =============================================================================

time = [merged.index[i].to_julian_date() for i in range(len(merged.index))]

    
X= time
Y=cols1
Z =merged.as_matrix().T
levels = np.logspace(0.01,1,1000)
x,y = np.meshgrid(X,Y)
plt.contourf(x,y,Z, levels=levels)
plt.yscale('log')
plt.ylim(0.2,1)


# =============================================================================
# xedges= np.linspace(min(x), max(x), 162)
# yedges  = np.logspace(min(y), max(y), 840)
# H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
# =============================================================================
