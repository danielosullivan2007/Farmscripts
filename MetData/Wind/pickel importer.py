# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:29:10 2017

@author: Daniel
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
degree_sign= u'\N{DEGREE SIGN}'
num2words={-15:'minus15',-16:'minus16',-17:'minus17',-18:'minus18',
           -19:'minus19',-20:'minus20',-21:'minus21',
           -22:'minus22', -23:'minus23', -24:'minus24',-25: 'minus25'}
#indir = ('/Users/Daniel/Desktop/Farmscripts/Pickels/')
indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
os.chdir(indir)
aps=pd.read_pickle(indir+"aps.p")
INPs =pd.read_pickle(indir+"INPs.p")
met = pd.read_pickle(indir+ "met.p")
wind = pd.read_pickle(indir+ "wind.p")
smps = pd.read_pickle(indir+"SMPS.p")
wind.rename(columns = {'Date':'wind_Date', 'Time':'wind_time'}, inplace = True)
smps.rename(columns = {'Date':'smps_Date', 'Time':'smps_time', 'Count': 'smps_count'}, inplace = True)
met.drop(['Battery Voltage', 'Unnamed: 0','Logger Temperature', '100cm Soil Temperature', '30cm Soil Temperature', 'Sunshine total since 0900'], axis =1, inplace = True)
aps.dropna(axis=0, inplace = True)
aps.sort_index(inplace = True)

for T in range (-25,-10, 5):
    df_INP = INPs.loc[INPs['T'] ==-15]
    df_INP=df_INP.groupby('Datetime',as_index=False).mean()
    df_INP = df_INP.set_index("Datetime", drop = True)
    df_INPtidy = df_INP.drop([u'start',  u'T'], axis =1)
    
    
    met_align = met.reindex(df_INP.index, method ='nearest')
    met_align['m_datetime']=pd.to_datetime(met_align['Date']+" "+met_align['Time'], dayfirst =True)
    met_align['deltatime']=(met_align.index-met_align['m_datetime'])/np.timedelta64(1,'h')
    met_align =met_align[met_align['deltatime']>-10]
    met_align =met_align[met_align['deltatime']<10]

    wind_align = wind.reindex(df_INP.index, method ='nearest')
    smps_align=smps.reindex(df_INP.index, method ='nearest')
    
    smps_align['s_datetime']=pd.to_datetime(smps_align['smps_Date']+" "+smps_align['smps_time'], dayfirst =True)
    smps_align['deltatime']=(smps_align.index-smps_align['s_datetime'])/np.timedelta64(1,'h')
    smps_align =smps_align[smps_align['deltatime']>-10]
    smps_align =smps_align[smps_align['deltatime']<10]

    aps_align = aps.reindex(df_INP.index, method = 'nearest')
    aps_align['a_datetime']=pd.to_datetime(aps_align['a_dates']+" "+aps_align['a_times'], yearfirst =True)
    aps_align['a_deltatime']=(aps_align.index-aps_align['a_datetime'])/np.timedelta64(1,'h')
    aps_align =aps_align[aps_align['a_deltatime']>-10]
    aps_align =aps_align[aps_align['a_deltatime']<10]

    #result = pd.concat([df_INP, met_align, wind_align, smps_align], axis =1)
    
    
    wind_tidy=wind_align.drop(['Unnamed: 0','Date Code','wind_Date', 'SRC_NAME','GEOG_AREA_NAME'], axis = 1)
    met_tidy = met_align.drop([u'Date', u'Time', 'm_datetime', 'deltatime'], axis =1)
    smps_tidy = smps_align.drop([u'smps_Date', u'smps_time', 's_datetime','deltatime',],axis =1)
    aps_tidy=aps_align.drop(['a_dates', 'a_times', 'a_datetime','a_deltatime'],axis =1)
    
    clean_result = pd.concat([df_INPtidy, met_tidy, wind_tidy, smps_tidy, aps_tidy], axis =1)
    clean_result.drop(" ", axis=1, inplace = True)
    clean_result.rename(index={'INP': 'Log10 INPs',
                               'Dry Bulb Temperature': ' Dry Bulb Temp', u'Dew Point Temperature':'Dew Point Temp','Grass Temperature':'Grass Temp',
                               'Concrete Temperature':'Concrete Temp','10cm Soil Temperature':'10cm Soil Temp','MEAN_WIND_DIR':'Av wind direction', 'MEAN_WIND_SPEED':'Av wind speed', 'MAX_GUST_DIR':'Max gust dir',
                               'MAX_GUST_SPEED':'max gust speed', 'smps_count':'smps total', 'a_count':'aps_total'},
                               columns={'INP': 'Log10 INPs', 'Dry Bulb Temperature': ' Dry Bulb Temp', u'Dew Point Temperature':'Dew Point Temp','Grass Temperature':'Grass Temp',
                                        'Concrete Temperature':'Concrete Temp','10cm Soil Temperature':'10cm Soil Temp','MEAN_WIND_DIR':'Av wind direction',
                                        'MEAN_WIND_SPEED':'Av wind speed', 'MAX_GUST_DIR':'Max gust dir', 'MAX_GUST_SPEED':'max gust speed', 'smps_count':'SMPS total', 'a_count':'APS total'}, inplace =True)
    corr = clean_result.corr()
    corr.to_csv(indir+"corr at" + num2words[T]+".csv")
minus15=pd.read_csv('corr atminus15.csv', index_col='Unnamed: 0')
minus20=pd.read_csv('corr atminus20.csv', index_col='Unnamed: 0')
minus25=pd.read_csv('corr atminus25.csv', index_col='Unnamed: 0')


x = np.square(minus15.loc[' Dry Bulb Temp':'APS total',['Log10 INPs']].values)
y = np.square(minus20.loc[' Dry Bulb Temp':'APS total',['Log10 INPs']].values)
z = np.square(minus25.loc[' Dry Bulb Temp':'APS total',['Log10 INPs']].values)


fig, ax = plt.subplots(figsize=(5, 5))
ax= plt.subplot(111)


index = minus15.index
index = index[1:16]
y_pos = np.arange(len(index))
ax.bar(y_pos-0.2, x, align = 'center', width=0.2, color = 'b', label ='-15 '+degree_sign+'C')
ax.bar(y_pos, y, align = 'center',width=0.2, color = 'r', label ='-20 '+degree_sign+'C')
ax.bar(y_pos+0.2, z, align = 'center',width=0.2, color = 'g', label ='-25 '+degree_sign+'C')
plt.xticks(y_pos,index, rotation = 90)
plt.xlim(-1,15)
plt.legend(loc=2, fontsize =10)
plt.ylabel('Pearson R Coefficient')
plt.ylim(0,1)
plt.tight_layout()
plt.savefig(indir+"\correlations")

#==============================================================================
# index = corr.index[1:]
# y_pos = np.arange(len(index))
# fig, ax = plt.subplots()
# ax= plt.subplot(111)
# plt.legend(loc=2, fontsize =10)
# plt.ylabel('Pearson R Coefficient')
# plt.ylim(-1,1)
# plt.tight_layout()
# plt.xticks(y_pos,index, rotation = 90)
# ax.bar(y_pos, x)
# 
#==============================================================================
