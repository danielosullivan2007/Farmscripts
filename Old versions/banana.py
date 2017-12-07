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
import matplotlib.ticker
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter, LogLocator, LogFormatterExponent,FormatStrFormatter,LogFormatterMathtext 
from matplotlib.colors import LogNorm
import matplotlib.colors as mplc


import time
start_time = time.time()



chi=1.2
rho0=1
rho=2.4

label=[]
xlabel =[]
cbar_labs=[]
dt=[]
dt_label=[]
hours =[]
q=[]
mask=[]

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

#==============================================================================
#'''TURN ON TO REPICKLE'''
# daily_aps  = aps.resample(timestep).mean().dropna(axis =0, how ='all')
# daily_smps  = smps.resample(timestep).mean().dropna(axis =0, how ='all')
# 
# daily_aps.to_pickle(farmdirs['pickels']+'daily_aps.p')
# daily_smps.to_pickle(farmdirs['pickels']+'daily_smps.p')
#==============================================================================

daily_aps = pd.read_pickle(farmdirs['pickels']+'daily_aps.p')
daily_smps = pd.read_pickle(farmdirs['pickels']+'daily_smps.p')


#%% Adding zeros
length, width = daily_aps.shape
start = daily_aps.index.min()
end= daily_aps.index.max()
index1=pd.date_range(start, end, freq = timestep)
zeros=np.zeros((len(index1), width))
zeros =pd.DataFrame(zeros, index= index1)

for i in range(len(index1)):
    if (daily_aps.index == index1[i]).any():
        mask.append(False)
    else:
        mask.append(True)
        
zeros.reset_index(inplace=True)
zeros.rename(columns = {'index':'datetime'}, inplace =True)	
mask = pd.Series(mask, name ='datetime')
zeros = zeros[mask]

daily_aps = daily_aps.reset_index()
cols = list(daily_aps)
zeros.columns = cols
to_plot= zeros.append(daily_aps)
to_plot = to_plot.sort_values(by='datetime')
to_plot.set_index('datetime', inplace =True)


merged=to_plot

#merged=merged['aps']
cols1=list(to_plot)

#%%
#Plotting section

time1 = [to_plot.index[i].to_julian_date() for i in range(len(to_plot.index))]

fig1=plt.figure()
ax1=plt.subplot(311)
X= time1
Y=cols1
p=to_plot.as_matrix().T
p[p==0]='nan'
Z = p
levels = np.logspace(-2,np.log10(np.nanmax(Z)),1000)
x,y = np.meshgrid(X,Y)

cmap=plt.cm.jet
cmap.set_under(color='k')
p1 = ax1.contourf(x,y,Z, levels=levels,cmap=plt.cm.jet,norm=matplotlib.colors.LogNorm(vmin=0.1,
                                                 vmax=np.nanmax(Z)))
ax1.set_yscale('log')
plt.ylabel('Aerodynamic Diameter ($\mu m$)', fontsize=8)
ax1.set_ylim(0.4,3)

#ax1.set_facecolor('black')
plt.ylim(0.4,1)
plt.draw()
plt.xlabel('Date')
plt.title('APS Time Series Plot')


#%%
#FORMAT X AND Y TICK LABELS
ticks = ax1.get_xticklabels()
#NEXT STEPS CHANGE JULIAN FORMATTING TO DATETIME
q = [item.get_text() for item in ax1.get_xticklabels()]
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
ax1.set_xticklabels(dt)

yticks = ax1.get_yticklabels()
ytick_labels= [item.get_text() for item in ax1.get_yticklabels()]
ax1.yaxis.set_minor_formatter(matplotlib.ticker.FormatStrFormatter("%.2f"))
ax1.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%.2f"))
#Colorbar 
cbaxes=fig1.add_axes([0.93, 0.7, 0.02, 0.2]) 

cbar = plt.colorbar(p1, ax=ax1,cax = cbaxes,
                    ticks = LogLocator(subs=range(10)) ,label='Count L$^{-1}$',
                   extend ='max', format=FormatStrFormatter('%.0e'))

cbar.ax.set_ylabel('Particle Count (L$^{-1}$)', fontsize = 10)
cbar.formatter = LogFormatterExponent(base=10) # 10 is the default
cbar.update_ticks()
cticks=cbar.ax.get_yticklabels()
cbticks = [item.get_text() for item in cbar.ax.get_yticklabels()]
[cbar_labs.append('') if cbticks[i]=='' else cbar_labs.append("$10^{%s}$"%str(cbticks[i]))
for i in range(len(cbticks))]
cbar.ax.set_yticklabels(cbar_labs)
del xlabel, q
print("APS Plotted after --- %s seconds ---" % (time.time() - start_time))
'''
##############################################################################
#
##############################################################################
'''
#%%
length, width = daily_smps.shape
start = daily_smps.index.min()
end= daily_smps.index.max()
index1=pd.date_range(start, end, freq = timestep)
zeros=np.zeros((len(index1), width))
zeros =pd.DataFrame(zeros, index= index1)
mask=[]
for i in range(len(index1)):
    if (daily_smps.index == index1[i]).any():
        mask.append(False)
    else:
        mask.append(True)
        
zeros.reset_index(inplace=True)
zeros.rename(columns = {'index':'datetimes'}, inplace =True)	
mask = pd.Series(mask, name ='datetimes')
zeros = zeros[mask]

daily_smps = daily_smps.reset_index()
cols = list(daily_smps)
zeros.columns = cols
to_plot= zeros.append(daily_smps)
to_plot = to_plot.sort_values(by='datetimes')
to_plot.set_index('datetimes', inplace =True)


merged=to_plot


cols1=list(to_plot)

time1 = [merged.index[i].to_julian_date() for i in range(len(merged.index))]
label=[]
xlabel =[]
cbar_labs=[]
dt=[]
dt_label=[]
hours =[]
q=[]

#SMPS Section
ax2=fig1.add_subplot(312, sharex=ax1)
X= time1
Y=cols1
p=merged.as_matrix().T
p[p==0]='nan'
Z = p
levels = np.logspace(-2,np.log10(np.nanmax(Z)),1000)
x,y = np.meshgrid(X,Y)
p1 = ax2.contourf(x,y,Z, levels=levels,cmap=plt.cm.jet,norm=matplotlib.colors.LogNorm(vmin=0.1,
                                                 vmax=np.nanmax(Z)))
ax2.set_yscale('log')
#plt.ylabel('Aerodynamic Diameter ($\mu m$)')
ax2.set_ylim(0.4,3)

#ax1.set_facecolor('black')
plt.ylim(0.01,1)
plt.draw()
plt.xlabel('Date')

("APS Plotted after --- %s seconds ---" % (time.time() - start_time))
#FORMAT X AND Y TICK LABELS
ticks = ax2.get_xticklabels()
#NEXT STEPS CHANGE JULIAN FORMATTING TO DATETIME
# =============================================================================
# q = [item.get_text() for item in ax2.get_xticklabels()]
# [xlabel.append('') if q[i]=='' else xlabel.append(float(q[i])+2.45765e6)for i in range(len(q))]
# [dt.append('') if q[i]=='' else dt.append(list(jd_to_date(xlabel[i])))for i in range(len(xlabel))]
# for i in range(len(dt)):
#     if dt[i]=='':
#         hours.append('')
#     else:
#         hours.append(dt[i][2]%1*24)
#         dt[i].append(int(hours[i]))
#         dt[i][2]=int(math.floor(dt[i][2]))
#         dt[i]=tuple(dt[i])
#         dt[i]=datetime.datetime(*dt[i])
#         dt[i]=datetime.datetime.strftime( dt[i].date(), '%d/%m')
# ax2.set_xticklabels(dt)
# 
# yticks = ax2.get_yticklabels()
# =============================================================================
ytick_labels= [item.get_text() for item in ax1.get_yticklabels()]
#ax2.yaxis.set_minor_formatter(matplotlib.ticker.FormatStrFormatter("%.f"))
ax2.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%.2f"))

#Colorbar 
#cbaxes=fig1.add_axes([0.93, 0.2, 0.02, 0.6]) 

# =============================================================================
# cbar = plt.colorbar(p1, ax=ax2,cax = cbaxes,
#                     ticks = LogLocator(subs=range(10)) ,label='Count L$^{-1}$',
#                    extend ='max', format=FormatStrFormatter('%.0e'))
# 
# cbar.ax.set_ylabel('Particle Count (L$^{-1}$)', fontsize = 10)
# cbar.formatter = LogFormatterExponent(base=10) # 10 is the default
# cbar.update_ticks()
# cticks=cbar.ax.get_yticklabels()
# cbticks = [item.get_text() for item in cbar.ax.get_yticklabels()]
# [cbar_labs.append('') if cbticks[i]=='' else cbar_labs.append("$10^{%s}$"%str(cbticks[i]))
# for i in range(len(cbticks))]
# cbar.ax.set_yticklabels(cbar_labs)
# 
# 
# =============================================================================
del cbticks, cols, DpAPS, DpSMPS, cbar_labs, dt
del dt_label, hours, i, label, levels, p, q, time1, smps_diameters, x,y
del xlabel, ytick_labels, cols1, rho, rho0
del chi, farmdirs

print("--- %s seconds ---" % (time.time() - start_time))