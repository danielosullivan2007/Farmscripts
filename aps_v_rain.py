# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 11:49:23 2017

@author: useradmin
"""
import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs
import numpy as np
import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import NullFormatter
from banana_support import INPs_25, INPs_24, INPs_18
aps_test = pd.read_pickle(farmdirs['pickels']+'aps_toplot_RH100.p')
aps=pd.read_pickle(farmdirs['pickels']+'aps.p')
aps.reset_index(drop=True, inplace =True)
aps.set_index(aps.datetime, inplace=True)
aps['tot']=aps.iloc[:,0:51].sum(axis=1)


####################create met data in julian time, also add hourly rain####
met_jd = pd.read_pickle(farmdirs['pickels']+'met_jd.p')
rain_cumul = met_jd['Rainfall Total since 0900']
met_jd['hourly_rain'] = rain_cumul.diff()

for i in range(len(met_jd)):
    if met_jd.index[i].time() == datetime.time(10, 0):
        met_jd['hourly_rain'][i] = 0

rain = []

for i in range(len(met_jd)):
    if met_jd['hourly_rain'][i]==0:
        rain.append('dry')
    else:
        rain.append('rain')
        
met_jd['rain']=rain
########################################################

aps_test = aps_test.sum(axis=1)
aps_test = aps_test[aps_test>0]
aps_test = pd.DataFrame(aps_test).rename(columns = {0:'aps'})
join= pd.merge(aps_test, met_jd, left_index=True, right_index=True)

#%%
RH = 0
title = 'RH >0%'
join['log_aps']=join['aps'].apply(np.log10)

start='2016-09-30'
end = '2016-10-01'
join = join.loc[start:end]
met=met_jd.loc[start:end]
aps=aps.loc[start:end]
#join = join.loc['2016-09-29':'2016-10-03']


join=join[join['Humidity']>RH]


join['start']=join.index
join['Date']=[join.start[i].date() for i in range(len(join))]

rainy_day=pd.DataFrame()
for i in pd.date_range(start=start, end=end):
    j = i.date()
    frame =join[join['Date'] == j]
    if frame.hourly_rain.any() >0:
        frame['rain_on_day']='Y'
    else:
        continue
    #print frame
    rainy_day  = rainy_day.append(frame)


# =============================================================================
# fig, axs = plt.subplots(10,1, figsize=(5, 40), facecolor='w', edgecolor='k')
# fig.subplots_adjust(hspace = .5, wspace=.001)
# 
# axs = axs.ravel()
# 
# c=0
# for i in pd.date_range(start=start, end=end):
#         j = i.date()
#         rain =rainy_day[rainy_day['Date'] == j]
#         if c<10:
#             if rain.empty:
#                 print 'empty'
#                 continue
#             else:            
#                 
#                     print rain['aps'].head(1)
#                     axs[c].plot(rain.index, rain['aps'], marker = 'o',markerfacecolor='r')
#                     axs[c].set_yscale('log')
#                     axs[c].text(0.1, 0.1, str(j), transform=axs[c].transAxes)
# 
#                     ax2=axs[c].twinx()
#                     ax2.plot(rain.index, rain['hourly_rain'], marker = 'o', markerfacecolor='b')
#                     c+=1
# =============================================================================
            

fig, ax1 = plt.subplots()

ax1.plot(join.index, join.hourly_rain, marker = 'o',alpha =0.2 )
ax1.plot(met.index, met['Rainfall Total since 0900'], marker = 'o',color = 'k', ls=':')
ax1.set_ylabel('Hourly Rainfall mm')
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
ax1.xaxis.set_minor_formatter(mdates.DateFormatter("%m-%d"))

plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))
plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=1))
plt.gca().xaxis.set_minor_formatter(NullFormatter())
plt.xticks(rotation = 30)
plt.xlabel('Date')

ax2=ax1.twinx()
ax2.plot(join.index, join.aps, marker = 'o',color = 'g', zorder =20 )
ax2.plot(aps.index, aps.tot, marker = 'o',color = 'r', ls=':', alpha =0.2)
ax2.set_yscale('log')
plt.xticks(rotation = 30)
ax2.set_ylabel('APS Total L$^{-1}$')


#==============================================================================
# import seaborn as sns
# 
# ax=sns.lmplot( 'hourly_rain', 'log_aps',data = join, hue = 'rain', fit_reg=False)
# cols = list(met_jd)
# #plt.ylim(0,100)
# plt.xlabel('Hourly Rain')
# plt.ylabel('log$_{10}$ APS Count')
# #plt.ylim(0,2.5)
# plt.text(100,2.1,title, color ='r')
# plt.savefig(farmdirs['figures']+ 'humidity_aps')
#==============================================================================
###################################################################
# =============================================================================
# smps_test = pd.read_csv(farmdirs['pickels']+'smps_RH100.csv')
# smps_test.set_index('datetime', inplace =True)
# smps_test = smps_test.sum(axis=1)
# smps_test = smps_test[smps_test>0]
# smps_test = pd.DataFrame(smps_test).rename(columns = {0:'smps'})
# join_smps= pd.merge(smps_test, met_jd, left_index=True, right_index=True)
# join_smps=join_smps[join_smps['Humidity']>RH]
# join_smps['log_smps']=join_smps['smps'].apply(np.log10)
# 
# #ax=sns.jointplot( 'Humidity', 'log_smps',data = join_smps, kind ='reg')
# cols = list(met_jd)
# #plt.ylim(0,100)
# plt.xlabel('% RH')
# plt.ylabel('log$_{10}$ SMPS Count')
# 
# plt.text(100,4.1,title, color ='r')
# =============================================================================
