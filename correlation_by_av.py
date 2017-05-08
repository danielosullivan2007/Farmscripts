# -*- coding: utf-8 -*-
"""
Created on Wed May 03 18:03:08 2017

@author: eardo
"""
import pandas as pd
import numpy as np
import os as os
import glob 
topfolder='W:\\'
key_terms= ["Data"]

timediff_end=pd.Series()
timediff_start=pd.Series()
timediffs=pd.DataFrame( columns= ['t_from_start', 't_from_end'])


num2words={-15:'minus15',-16:'minus16',-17:'minus17',-18:'minus18',
           -19:'minus19',-20:'minus20',-21:'minus21',
           -22:'minus22', -23:'minus23', -24:'minus24',-25: 'minus25'}
           
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

smps_avs = pd.DataFrame(columns = [u'datetime',    u' 14.1',    u' 14.6',    u' 15.1',    u' 15.7',
          u' 16.3',    u' 16.8',    u' 17.5',    u' 18.1',    u' 18.8',
          u'358.7',    u'371.8',    u'385.4',    u'399.5',    u'414.2',
          u'429.4',    u'445.1',    u'461.4',    u'478.3',    u'495.8'])
######################################################################################################
#==============================================================================
# indir = ('W:\SMPS')
# 
# os.chdir(indir)
# df_smps = pd.DataFrame(columns= ['NaT',u'Date', u'Start Time',u' 14.1', u' 14.6',u' 15.1',u' 15.7',u' 16.3',
#  u' 16.8',u' 17.5', u'514.0',u'532.8',u'552.3',u'572.5',u'593.5',u'615.3',u'637.8',u'661.2',u'685.4', u'710.5'])
# a=glob.glob('*.csv')
# 
# for i in range(len(a)):
#     df=pd.read_csv(a[9], delimiter =',', header =25, skip_footer=30)
#     df=df.drop(df.index[2:8])
#     df.loc[-1] = pd.to_datetime(df.iloc[0][1:]+" "+df.iloc[1][1:])
#     df.index = df.index + 1  # shifting index
#     df = df.sort()  # sorting by index
#     df = df.transpose()
#     df=df.set_index(df[0])
#     df.columns = df.iloc[0][:]
#     df=df.drop(df.index[0])
#     df_smps = df_smps.append(df)
# 
# df_smps.to_pickle('C:\Users\eardo\Desktop\Farmscripts\Pickels\smps.p')
#==============================================================================
#########################################################################################################
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




##############################################################################################################################
#indir = ('/Users/Daniel/Desktop/Farmscripts/Pickels/')
indir = ('C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\')
os.chdir(indir)
aps=pd.read_pickle(indir+"aps.p")
INPs =pd.read_pickle(indir+"INPs.p")
met = pd.read_pickle(indir+ "met.p")
wind = pd.read_pickle(indir+ "wind.p")
smps = pd.read_pickle(indir+"SMPS.p")
#smps=smps.drop([u'<0.523', u'Aerodynamic Diameter', u'Date',
       #u'Start Time'], axis =0)

smps = smps.rename(columns ={'index':'datetime'})


for T in range (-25,-10, 5):
    df_INP = INPs.loc[INPs['T'] ==T]
    #df_INP['timedelta']= df_INP['end_datetime']-df_INP['start_datetime']

    
    df_INPtidy = df_INP.drop([ u'T'], axis =1).reset_index()
    
    df_INPtidy = df_INPtidy.drop('index', axis=1)
    met.reset_index(inplace=True)
    
    for i in range (len(df_INPtidy)):
        metmask=(met['Datetime'] > df_INPtidy['start_datetime'][i]) & (met['Datetime'] <=  df_INPtidy['end_datetime'][i])
        
        metavs = metavs.append(met.loc[metmask].mean(axis=0), ignore_index=True)
    metavs.drop([u'index', u'Unnamed: 0',u'level_0'], axis=1)
    
        
    wind.reset_index(inplace=True)
    for i in range (len(df_INPtidy)):
        
        smps_mask = (smps['datetimes'] > df_INPtidy['start_datetime'][i]) & (smps['datetimes']  <=  df_INPtidy['end_datetime'][i])
        smps_avs=smps_avs.append(smps.loc[smps_mask].mean(axis=0, skipna = True), ignore_index=True)
        diff_to_end= (smps.loc[smps_mask]['datetimes'].iloc[-1] - df_INPtidy['end_datetime'][i]) #/ pd.Timedelta('1 hour')
        diff_from_start = (smps.loc[smps_mask]['datetimes'].iloc[0] - df_INPtidy['start_datetime'][i]) 
        
#==============================================================================
#         timediff_start=timediff_start.set_value(i, diff_from_start)
#         timediff_end=timediff_end.set_value(i, diff_to_end)
#         
#         timediffs=pd.DataFrame([timediff_start, timediff_end])
#         timediffs=timediffs.transpose()
#         timediffs = timediffs/ np.timedelta64(1, 'h')
#         smps_total = smps_avs.sum(axis=1)
#         smps_total.columns='SMPS_total'
#==============================================================================
    
    
    aps=pd.read_pickle(indir+"aps.p")
    for i in range(len(df_INPtidy)):
        aps_mask=  (aps['datetime'] > df_INPtidy['start_datetime'][i]) & (aps['datetime'] <=  df_INPtidy['end_datetime'][i])
        apsavs=apsavs.append(aps.loc[aps_mask].mean(axis=0), ignore_index=True)
        aps_total= apsavs.sum(axis=1)
        
    
    
    for i in range (len(df_INPtidy)):
        windmask=(wind['OB_END_TIME'] > df_INPtidy['start_datetime'][i]) & (wind['OB_END_TIME'] <=  df_INPtidy['end_datetime'][i])
        
        windavs = windavs.append(wind.loc[windmask].mean(axis=0), ignore_index= True)
    windavs=windavs.drop(u'Unnamed: 0', axis=1)
    
    data=pd.concat([df_INPtidy, windavs, metavs, aps_total, smps_total], axis =1)
    data=data.drop([u'index', 'Datetime', u'Unnamed: 0', u'level_0'], axis=1)
    
    
    corr=data.corr()
#==============================================================================
#     corr = corr.drop(['100cm Soil Temperature','30cm Soil Temperature','Battery Voltage', 'Logger Temperature',
#      'Sunshine total since 0900', 'Date', 'Time', ' '], axis =1)
#==============================================================================
    
    corr.rename(columns = {u'Dry Bulb Temperature':'Dry Bulb T', u'Dew Point Temperature': 'Dew Point T', u'Grass Temperature':'Grass T', 
    u'Concrete Temperature': 'Concrete T', u'10cm Soil Temperature': 'Soil T', u'Rainfall Total since 0900': 'Rainfall Total',
     u'Radiation Total since 0900': 'Radiation Total',  0L: 'APS Total Count' , 1L: 'SMPS Total Count'}, inplace = True)

    corr.to_csv(indir+"corr at" + num2words[T]+".csv")
    print 'done'
    