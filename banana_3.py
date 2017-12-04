"""
Created on Mon Nov 06 10:54:13 2017
@author: eardo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs
import datetime
from myfuncs import jd_to_date
import time
import math
import matplotlib.ticker
import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import LogFormatter, MaxNLocator, LogLocator, LogFormatterExponent,FormatStrFormatter,LogFormatterMathtext 
from matplotlib.colors import LogNorm
import time
from banana_support import INPs_25, INPs_20, INPs_18, INPs_24

direction = '>'
RH = 0

start_time = time.time()

timestep = '1H'

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
aps=aps[aps.index<'2016-10-31']
#%%
aps_diameters = np.array([float(i) for i in list(aps)])
smps_diameters =np.array([float(i) for i in list(smps)])/1000

DpAPS=np.round((((chi*rho0)/rho)**0.5)*aps_diameters,2)
DpSMPS=np.round((1/chi)*smps_diameters,3)


aps.columns = DpAPS
smps.columns  = DpSMPS

del i, aps_diameters


daily_aps  = aps.resample(timestep).mean().dropna(axis =0, how ='all')
daily_smps  = smps.resample(timestep).mean().dropna(axis =0, how ='all')

daily_aps.to_pickle(farmdirs['pickels']+'daily_aps.p')
daily_smps.to_pickle(farmdirs['pickels']+'daily_smps.p')

daily_aps = pd.read_pickle(farmdirs['pickels']+'daily_aps.p')
daily_smps = pd.read_pickle(farmdirs['pickels']+'daily_smps.p')


#FILTERING BY HUMIDITY
met_filt = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
join= pd.concat([daily_aps, met_filt],join = 'outer', axis=1)
cols = list(join)
join['Humidity'].fillna(0, inplace =True)

if direction == '<':
    b =join[join['Humidity']<RH]
elif direction == '>':
    b =join[join['Humidity']>RH]

aps_filtered = b.iloc[:,0:50].reset_index().rename(columns= {'index':'datetime'})


######


#FILTERING BY HUMIDITY
met_filt = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
join= pd.concat([daily_smps, met_filt],join = 'outer', axis=1)
cols = list(join)
join['Humidity'].fillna(0, inplace =True)
if direction == '<':
    a =join[join['Humidity']<RH]
elif direction == '>':
    a =join[join['Humidity']>RH]

smps_filtered = a.iloc[:,0:111].reset_index().rename(columns= {'index':'datetime'})


######

#%% Adding zeros
length, width = daily_aps.shape
start = daily_aps.index.min()
end= daily_aps.index.max()
index1=pd.date_range(start, end, freq = timestep)
zeros=np.zeros((len(index1), width))
zeros =pd.DataFrame(zeros, index= index1)
mask=[]



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
aps_toplot= zeros.append(aps_filtered)
aps_toplot.fillna(0, inplace =True)
aps_toplot = aps_toplot.sort_values(by='datetime')
aps_toplot.set_index('datetime', inplace =True)
#TURN THIS ON TO GET PICKLE OF RH =100
#aps_toplot.to_pickle(farmdirs['pickels']+'aps_toplot_RH100.p')



#merged=merged['aps']



'''
##############################################################################
#
##############################################################################
'''
#%%
daily_smps.reset_index(inplace =True)
length, width = daily_smps.set_index('datetimes').shape
start = daily_smps.set_index('datetimes').index.min()
end= daily_smps.set_index('datetimes').index.max()
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
cols = list(daily_smps)
zeros.columns = cols
zeros.rename(columns = {'index':'datetimes'}, inplace =True)
zeros.rename(columns = {'datetimes':'datetime'}, inplace =True)


cola = list(smps_filtered)
colb = list(zeros)
zeros.drop(zeros.columns[1:25], axis =1, inplace =True)
smps_filtered.drop(smps_filtered.columns[1:25], axis =1, inplace =True)
to_plot= zeros.append(smps_filtered)
to_plot = to_plot.sort_values(by='datetime')
to_plot.set_index('datetime', inplace =True)
to_plot.to_csv(farmdirs['pickels']+'smps_RH100.csv')

merged=to_plot


cols1=list(to_plot)

time1 = [merged.index[i].to_julian_date() for i in range(len(merged.index))]

cbar_labs=[]

q=[]

'''
##############################################################
'''


met = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
met = met.resample(timestep).mean()

rain_cumul = met['Rainfall Total since 0900']
met['hourly_rain'] = rain_cumul.diff()

for i in range(len(met)):
    if met.index[i].time() == datetime.time(10, 0):
        met['hourly_rain'][i] = 0
rain =[]
for i in range(len(met)):
    if met['hourly_rain'][i]==0:
        rain.append('dry')
    else:
        rain.append('rain')
        
met['rain']=rain              


from myfuncs import mask
met = mask(met, daily_aps)

if direction =='<':
    met = met[met['Humidity']<RH]
elif direction =='>':
    met = met[met['Humidity']>RH]

'''###########################################################################
'''

print("--- %s seconds ---" % (time.time() - start_time))

fig1=plt.figure()
ax1=plt.subplot(611)
ax1.plot(INPs_24.mid_jd, INPs_24.INP, marker ='o',
         markersize = 5 , linestyle ='dashed', markerfacecolor='r')
ax1.tick_params(labelbottom='off')
plt.yscale('log')
plt.ylabel('INPs ($L^{-1}$)', fontsize =8)

# =============================================================================
# ax5=fig1.add_subplot(615, sharex=ax1)
# ax5.plot(INPs_20.mid_jd, INPs_20.INP, marker ='o',
#          markersize = 5 , linestyle ='dashed', markerfacecolor='r')
# ax5.tick_params(labelbottom='off')
# plt.yscale('log')
# plt.ylabel('INPs ($L^{-1}$)', fontsize =8)
# =============================================================================

ax2=fig1.add_subplot(612, sharex=ax1)
ax2.plot(INPs_18.mid_jd, INPs_18.INP, marker ='o',
         markersize = 5 , linestyle ='dashed', markerfacecolor='r')

plt.yscale('log')
plt.ylabel('INPs ($L^{-1}$)', fontsize =8)
plt.xlim(2457655, 2457693.1666666665)
################################################################################



ax3=fig1.add_subplot(613, sharex=ax1)
dry=met['rain'] == 'dry'
rain=met['rain'] == 'rain'

ax3.plot(met.jd[dry], met.Humidity[dry], marker = 'o', linewidth = 0, markersize=3)
ax3.plot(met.jd[rain], met.Humidity[rain], marker = 'o', linewidth = 0, markersize=3, color ='r')

plt.ylabel('% RH', fontsize =8)
ax3.yaxis.set_major_locator(MaxNLocator(4))
ax3.tick_params(labelbottom='off')  


#%%
#Plotting section

time1 = [aps_toplot.index[i].to_julian_date() for i in range(len(aps_toplot.index))]
cols1=list(aps_toplot)


ax4=fig1.add_subplot(614, sharex=ax1)
X= time1
Y=cols1
p=aps_toplot.as_matrix().T
#p[p==0]='nan'
Z = p
levels = np.logspace(-2,2.5,500)
x,y = np.meshgrid(X,Y)

cmap=plt.cm.jet
cmap.set_under(color='k')
cmap.set_over(color='red')
p1 = ax4.contourf(x,y,Z, levels=levels,cmap=plt.cm.jet,norm=matplotlib.colors.LogNorm(vmin=0.1,
                                                 vmax=np.nanmax(Z)))

plt.ylabel('APS \n D$_p (\mu m$)', fontsize =8)
#ax1.set_ylim(0.4,3)

#ax1.set_facecolor('black')
#plt.ylim(0.4,1)
plt.draw()
#plt.xlabel('Date')
plt.title('Time Series Plots RH {}{}%'.format(direction, RH))
plt.yticks([])
ax4.set_ylim(0.4,1.5)
plt.yscale('log', subsy=[0.5,  0.75])

yticks = ax4.get_yticklabels()
ytick_labels= [item.get_text() for item in ax1.get_yticklabels()]
ax4.yaxis.set_minor_formatter(matplotlib.ticker.FormatStrFormatter("%.2f"))
ax4.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%.2f"))



#%%
#FORMAT X AND Y TICK LABELS
plt.xlim(2457655, 2457690.1666666665)
ticks = ax4.get_xticklabels()
plt.draw()
#NEXT STEPS CHANGE JULIAN FORMATTING TO DATETIME
q = [item.get_text() for item in ax4.get_xticklabels()]
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
ax4.set_xticklabels(dt)

ax4.tick_params(labelbottom='off')  


#Colorbar 
cbaxes=fig1.add_axes([0.93, 0.75, 0.02, 0.15]) 

cbar = plt.colorbar(p1, ax=ax4,cax = cbaxes,
                    ticks = LogLocator(subs=range(10)) ,
                   extend ='max', format=FormatStrFormatter('%.0e'))

cbar.ax.set_ylabel('Number (L$^{-1}$)', fontsize = 10)
cbar.ax.minorticks_off()
cbar.formatter = LogFormatterExponent(base=10) # 10 is the default
cbar.update_ticks()
cticks=cbar.ax.get_yticklabels()
cbticks = [item.get_text() for item in cbar.ax.get_yticklabels()]
[cbar_labs.append('') if cbticks[i]=='' else cbar_labs.append("$10^{%s}$"%str(cbticks[i]))
for i in range(len(cbticks))]
cbar.ax.set_yticklabels(cbar_labs)
del xlabel, q
print("APS Plotted after --- %s seconds ---" % (time.time() - start_time))



####################################################################################
#SMPS Section
ax5=fig1.add_subplot(615, sharex=ax1)
X= time1
Y=cols1
p=merged.as_matrix().T
p[p==0]='nan'
Z = p
levels = np.logspace(np.log10(0.02),np.log10(np.nanmax(Z)),500)
x,y = np.meshgrid(X,Y)
p2 = ax5.contourf(x,y,Z, levels=levels,cmap=plt.cm.jet,
                  norm=matplotlib.colors.LogNorm(vmin=np.min([Z[Z>0.001]]),
                                                 vmax=np.nanmax(Z)))
ax5.set_yscale('log')
plt.ylabel('SMPS \n D$_p (\mu m$)', fontsize =8)
cmap.set_under(color='k')

#ax1.set_facecolor('black')
plt.ylim(0.03,0.7)
plt.draw()


("APS Plotted after --- %s seconds ---" % (time.time() - start_time))
#FORMAT X AND Y TICK LABELS
#ax2.tick_params(labelbottom='off')

#COLORBAR
cbaxes=fig1.add_axes([0.93, 0.55, 0.02, 0.15]) 

cbar = plt.colorbar(p2, ax=ax5,cax = cbaxes,
                    ticks = LogLocator(subs=range(10)) ,label='Count L$^{-1}$',
                   extend ='max', format=FormatStrFormatter('%.0e'))

#cbar.ax.set_ylabel('Particle Count (L$^{-1}$)', fontsize = 10)
cbar.formatter = LogFormatterExponent(base=10) # 10 is the default
cbar.update_ticks()
cticks=cbar.ax.get_yticklabels()
cbticks = [item.get_text() for item in cbar.ax.get_yticklabels()]
[cbar_labs.append('') if cbticks[i]=='' else cbar_labs.append("$10^{%s}$"%str(cbticks[i]))
for i in range(len(cbticks))]
cbar.ax.set_yticklabels(cbar_labs)

###########################################################################################
del cbticks, cols, DpAPS, DpSMPS, cbar_labs, timestep, time1, x, y, zeros
del rho, rho0,   smps_diameters, mask, width, start_time
del ytick_labels, start, p, INPs_20, INPs_25, X,Y,Z, cola, colb, cols1, direction
del dt, end, farmdirs, hours, index1, levels, length, i, a, b