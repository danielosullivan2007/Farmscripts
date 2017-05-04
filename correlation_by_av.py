# -*- coding: utf-8 -*-
"""
Created on Wed May 03 18:03:08 2017

@author: eardo
"""
import pandas as pd
import os as os
import glob 
topfolder='W:\\'
key_terms= ["Data"]


metavs=pd.DataFrame(columns=[u'level_0', u'index',
       u'Dry Bulb Temperature', u'Dew Point Temperature', u'Grass Temperature',
       u'Concrete Temperature', u'10cm Soil Temperature',
       u'Rainfall Total since 0900', u'Radiation Total since 0900',
       u'Humidity'])

windavs =pd.DataFrame(columns=['MEAN_WIND_DIR', 'MEAN_WIND_SPEED', 
'MAX_GUST_DIR', 'MAX_GUST_SPEED', 'MAX_GUST_CTIME'])

apsavs= pd.DataFrame(columns =[u'0.542', u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835',
       u'0.898', u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382',
       u'1.486', u'1.596', u'1.715', u'1.843', u'1.981', u'10.37', u'11.14',
       u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
       u'19.81', u'2.129', u'2.288', u'2.458', u'2.642', u'2.839', u'3.051',
       u'3.278', u'3.523', u'3.786', u'4.068', u'4.371', u'4.698', u'5.048',
       u'5.425', u'5.829', u'6.264', u'6.732', u'7.234', u'7.774', u'8.354',
       u'8.977', u'9.647', u'<0.523', u'Aerodynamic Diameter', u'Date',
       u'Start Time', u'datetime'])

#indir = ('/Users/Daniel/Desktop/Farmscripts/Pickels/')
indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
os.chdir(indir)
aps=pd.read_pickle(indir+"aps.p")
INPs =pd.read_pickle(indir+"INPs.p")
met = pd.read_pickle(indir+ "met.p")
wind = pd.read_pickle(indir+ "wind.p")
smps = pd.read_pickle(indir+"SMPS.p")


for T in range (-25,-20, 5):
    df_INP = INPs.loc[INPs['T'] ==-25]
    df_INP['timedelta']= df_INP['end_datetime']-df_INP['start_datetime']

    
    df_INPtidy = df_INP.drop([ u'T'], axis =1).reset_index()
    met.reset_index(inplace=True)
for i in range (len(df_INPtidy)):
    metmask=(met['Datetime'] > df_INPtidy['start_datetime'][i]) & (met['Datetime'] <=  df_INPtidy['end_datetime'][i])
    
    metavs = metavs.append(met.loc[metmask].mean(axis=0), ignore_index=True)
metavs.drop([u'index', u'Unnamed: 0',u'level_0'], axis=1)

    
wind.reset_index(inplace=True)

for i in range (len(df_INPtidy)):
    windmask=(wind['OB_END_TIME'] > df_INPtidy['start_datetime'][i]) & (wind['OB_END_TIME'] <=  df_INPtidy['end_datetime'][i])
    
    windavs = windavs.append(wind.loc[windmask].mean(axis=0), ignore_index= True)
windavs=windavs.drop(u'Unnamed: 0', axis=1)
    


#==============================================================================
# indir = ('W:\APS')
# 
# os.chdir(indir)
# 
# a=glob.glob('*.csv')
# df_out=pd.DataFrame(columns =[u'Date', u'Start Time', u'Aerodynamic Diameter', u'<0.523', u'0.542',
#        u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835', u'0.898',
#        u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382', u'1.486',
#        u'1.596', u'1.715', u'1.843', u'1.981', u'2.129', u'2.288', u'2.458',
#        u'2.642', u'2.839', u'3.051', u'3.278', u'3.523', u'3.786', u'4.068',
#        u'4.371', u'4.698', u'5.048', u'5.425', u'5.829', u'6.264', u'6.732',
#        u'7.234', u'7.774', u'8.354', u'8.977', u'9.647', u'10.37', u'11.14',
#        u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
#        u'19.81', u'datetime'])
# 
# for i in range(len(a)):
#     df=pd.read_csv(a[i], delimiter =',', header =6).iloc[:, 1:56]
#     df['datetime']=pd.to_datetime(df['Date']+" "+df['Start Time'])
#     df=df.drop(u'Aerodynamic Diameter', axis=1)
#     df_out = df_out.append(df)
# 
# df_out.to_pickle(indir+"APS.p")
#==============================================================================

aps=pd.read_pickle(indir+"aps.p")
for i in range(len(df_INPtidy)):
    aps_mask=  (aps['datetime'] > df_INPtidy['start_datetime'][i]) & (aps['datetime'] <=  df_INPtidy['end_datetime'][i])
    apsavs=apsavs.append(aps.loc[aps_mask].mean(axis=0), ignore_index=True)
    aps_total= apsavs.sum(axis=1)
    
data=pd.concat([df_INPtidy, windavs, metavs, aps_total], axis =1)
data=data.drop([u'index', 'Datetime', u'Unnamed: 0', u'level_0'], axis=1)

corr=data.corr()


