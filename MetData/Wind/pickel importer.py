# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:29:10 2017

@author: Daniel
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
degree_sign= u'\N{DEGREE SIGN}'

indir = ('/Users/Daniel/Desktop/farmscripts/Pickels/')
os.chdir(indir)

INPs =pd.read_pickle(indir+"INPs.p")
met = pd.read_pickle(indir+ "met.p")
wind = pd.read_pickle(indir+ "wind.p")
smps = pd.read_pickle(indir+"SMPS.p")
wind.rename(columns = {'Date':'wind_Date', 'Time':'wind_time'}, inplace = True)
smps.rename(columns = {'Date':'smps_Date', 'Time':'smps_time', 'Count': 'smps_count'}, inplace = True)
met.drop(['Battery Voltage', 'Unnamed: 0','Logger Temperature', '100cm Soil Temperature', '30cm Soil Temperature', 'Sunshine total since 0900'], axis =1, inplace = True)



df15 = INPs.loc[INPs['T'] ==-15]
df15=df15.groupby('Datetime',as_index=False).mean()
df15 = df15.set_index("Datetime", drop = True)
df15_tidy = df15.drop([u'start',  u'T'], axis =1)


met_align = met.reindex(df15.index, method ='nearest')
wind_align = wind.reindex(df15.index, method ='nearest')
smps_align=smps.reindex(df15.index, method ='nearest')
result = pd.concat([df15, met_align, wind_align, smps_align], axis =1)

wind_tidy=wind_align.drop(['Unnamed: 0','Date Code','wind_Date', 'SRC_NAME','GEOG_AREA_NAME'], axis = 1)
met_tidy = met_align.drop([u'Date', u'Time'], axis =1)
smps_tidy = smps_align.drop([u'smps_Date', u'smps_time'],axis =1)


clean_result = pd.concat([df15_tidy, met_tidy, wind_tidy, smps_tidy], axis =1)
clean_result.drop(" ", axis=1, inplace = True)
clean_result.rename(columns={'INP': 'Log10 INPs', 'Dry Bulb Temperature': ' Dry Bulb Temp', u'Dew Point Temperature':'Dew Point Temp','Grass Temperature':'Grass Temp', 'Concrete Temperature':'Concrete Temp','10cm Soil Temperature':'10cm Soil Temp','MEAN_WIND_DIR':'Av_wind_direction', 'MEAN_WIND_SPEED':'Av_wind_speed', 'MAX_GUST_DIR':'Max gust dir', 'MAX_GUST_SPEED':'max gust speed'}, inplace =True)
corr = clean_result.corr()

x = corr.loc[' Dry Bulb Temp':'smps_count',['Log10 INPs']].values

index = corr.index[1:]
y_pos = np.arange(len(index))
fig, ax = plt.subplots()
ax= plt.subplot(111)

ax.bar(y_pos, x)