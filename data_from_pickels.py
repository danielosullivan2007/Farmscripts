# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 05:22:09 2017

@author: useradmin
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import socket

'''This portion of the script assembles pickles created, cleans files, and then does correlation analysis'''

indir = ('C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\')
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

#==============================================================================
# wind['Date Code']=wind['Date Code'].astype(str)
# for i in range(len(wind['Date Code'])):
#     print i
#     wind['wind_Date'][i]=wind['Date Code'][i][0:2]+"-"+wind['Date Code'][i][2:4]+"-"+wind['Date Code'][i][4:6]+' '+wind['Date Code'][i][6:8]+':'+wind['Date Code'][i][8:10]
# )
# wind.to_pickle('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\wind.p')
#==============================================================================
wind.wind_Date=pd.to_datetime(wind.wind_Date, yearfirst=True)

for T in range (-25,-10, 5):
    df_INP = INPs.loc[INPs['T'] ==T]
    df_INP=df_INP.groupby('Datetime',as_index=False).mean()
    df_INP = df_INP.set_index("Datetime", drop = True)
    #df_INPtidy = df_INP.drop([u'start',  u'T'], axis =1)
    
    #aligns data to closest member of INP dataframe by time, removes any values where difference is too high
    met_align = met.reindex(df_INP.index, method ='nearest')
    met_align['m_datetime']=pd.to_datetime(met_align['Date']+" "+met_align['Time'], dayfirst =True)
    met_align['deltatime']=(met_align.index-met_align['m_datetime'])/np.timedelta64(1,'h')
    met_align =met_align[met_align['deltatime']>-10]
    met_align =met_align[met_align['deltatime']<10]

    wind_align = wind.reindex(df_INP.index, method ='nearest')
    wind_align['deltatime']=(wind_align.index-wind_align['wind_Date'])/np.timedelta64(1,'h')
    
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
    
    
    wind_tidy=wind_align.drop(['Unnamed: 0','Date Code','wind_Date', 'SRC_NAME','GEOG_AREA_NAME','deltatime'], axis = 1)
    met_tidy = met_align.drop([u'Date', u'Time', 'm_datetime', 'deltatime'], axis =1)
    smps_tidy = smps_align.drop([u'smps_Date', u'smps_time', 's_datetime','deltatime',],axis =1)
    aps_tidy=aps_align.drop(['a_dates', 'a_times', 'a_datetime','a_deltatime'],axis =1)
    
    clean_result = pd.concat([df_INPtidy, met_tidy, wind_tidy, smps_tidy, aps_tidy], axis =1)
    
    
    clean_result.rename(index={'INP': 'Log10 INPs',
                               'Dry Bulb Temperature': ' Dry Bulb Temp', u'Dew Point Temperature':'Dew Point Temp','Grass Temperature':'Grass Temp',
                               'Concrete Temperature':'Concrete Temp','10cm Soil Temperature':'10cm Soil Temp','MEAN_WIND_DIR':'Av wind direction', 'MEAN_WIND_SPEED':'Av wind speed', 'MAX_GUST_DIR':'Max gust dir',
                               'MAX_GUST_SPEED':'max gust speed', 'smps_count':'smps total', 'a_count':'aps_total'},
                               columns={'INP': 'Log10 INPs', 'Dry Bulb Temperature': ' Dry Bulb Temp', u'Dew Point Temperature':'Dew Point Temp','Grass Temperature':'Grass Temp',
                                        'Concrete Temperature':'Concrete Temp','10cm Soil Temperature':'10cm Soil Temp','MEAN_WIND_DIR':'Av wind direction',
                                        'MEAN_WIND_SPEED':'Av wind speed', 'MAX_GUST_DIR':'Max gust dir', 'MAX_GUST_SPEED':'max gust speed', 'smps_count':'SMPS total', 'a_count':'APS total'}, inplace =True)
    clean_result.drop([u'Max gust dir', u'Av wind direction', u'MAX_GUST_CTIME'," "], axis=1, inplace = True)
    
    
    corr = clean_result.corr(method = 'pearson')
    corr.to_csv(indir+"corr at" + num2words[T]+".csv")