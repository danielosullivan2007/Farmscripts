# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:03:44 2017

@author: eardo
"""
import pandas as pd
from directories import farmdirs
import datetime


met = pd.read_pickle(farmdirs['pickels']+'met.p')

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
        


import matplotlib.pyplot as plt
fig, ax =plt.subplots()
ax.plot(met.index, met['hourly_rain'])


met_hourly = met.resample('1H').mean()
ax.set_ylim(-1, 6)
ax2 = ax.twinx()
ax2.plot(met_hourly.index, met_hourly['Humidity'], color ='r')
ax2.set_ylim(60, 120)


fig2, ax3=plt.subplots()
x=met['hourly_rain']
y=met['Humidity']
ax3 = plt.scatter(x, y)