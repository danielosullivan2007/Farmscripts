# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:22:25 2017

@author: eardo
"""
import os 
import pandas as pd
from datetime import datetime
from myfuncs import num2words
import seaborn as sns
import matplotlib.pyplot as plt
import socket

host = socket.gethostname()

if host == 'see4-234':
    os.chdir('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
    
    picdir = 'C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\'

else: 
    os.chdir('C:\\Users\\useradmin\\Desktop\\Farmscripts\\')
    picdir = 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\'



df=pd.read_csv('observations.csv')


fmt='%y%m%d'
new_cols = ['date','Datestr',
 'timestr',
 'Comments',
 'Agri_activitiy',
 'Met',
 'Haze']


def dateformat(df):
    df['date']=pd.to_datetime(df.Datestr, format =fmt, box =False).dt.date

    return df

def reorder_cols(df):
    #run cols =df.columns.tolist
    #newcols=new order
    df=df[new_cols]
    return df

def fill_na(df):
    df.fillna(value=0, inplace =True)
    return df

dateformat(df)
fill_na(df)
df= reorder_cols(df)
cleaned = df.drop(['Datestr', 'timestr', 
                   'Comments'], axis =1).rename(columns ={'Agri_activitiy':'Agri'})
features=['Agri', 'Haze']
processed =pd.get_dummies(cleaned, columns=features, drop_first =True)
processed.set_index('date', inplace =True)

data ={i: pd.read_csv(picdir + "data at "+num2words[i]+".csv")for i in range(-25, -10, 5)}
    
minus15=data[-15]   
minus15['date']=pd.to_datetime(minus15['2'], box =False).dt.date
minus15.set_index('date', inplace =True)

merged =processed.merge(minus15, how='outer', left_index=True, right_index=True)
merged.drop(merged.index[0:4], inplace =True)
merged = merged[['2',
 '3', 'Met',
 'Agri_Tractor',
 'Haze_Y',
 'Unnamed: 0',
 'INP',
 'MEAN_WIND_SPEED',
 'MAX_GUST_DIR',
 'MAX_GUST_SPEED',
 'MAX_GUST_CTIME',
 'Dry Bulb Temperature',
 'Dew Point Temperature',
 'Grass Temperature',
 'Concrete Temperature',
 '10cm Soil Temperature',
 'Rainfall Total since 0900',
 'Radiation Total since 0900',
 'Humidity',
 '0',
 'APS Total',
 '1',
 'SMPS Total',
 'demott']]
#merged.reset_index(inplace =True)
merged.Agri_Tractor.fillna(0, inplace =True)
final  = merged.dropna(axis =0, subset =['Agri_Tractor', 'INP'])
import numpy as np
final['day']=final.index
ax=final[final['Agri_Tractor'] ==0].INP.plot(marker='o', lw=0.1)
ax=final[final['Agri_Tractor'] ==1].INP.plot(marker='o', lw=0.1, color ='r')

#sns.tsplot(final.INP[final.Agri_Tractor==1], time =final.day[final.Agri_Tractor==1], interpolate=False, condition='Acitivy', color='r')
#sns.tsplot(final.INP[final.Agri_Tractor==0], interpolate=False, condition='no Acitivy')

#sns.tsplot(final.INP[final.Agri_Tractor==1], interpolate=False, condition='Acitivy')


import matplotlib.dates as mdates
myFmt = mdates.DateFormatter('%m/%d')


from matplotlib.ticker import MultipleLocator, FormatStrFormatter

majorLocator = MultipleLocator(4)

minorLocator = MultipleLocator(5)

ax.xaxis.set_major_locator(majorLocator)

ax.xaxis.set_minor_locator(minorLocator)
ax.set_ylabel('log10 [INP]')
ax.xaxis.set_major_formatter(myFmt)
ax.legend(['No activity','Agricultural activity'], loc = 'top right')
#%%


APS = pd.read_pickle(picdir+'aps.p')
df_APS =APS
myFmt = mdates.DateFormatter('%m/%dm')

APS_cols=[u'Date',
       u'Start Time', u'datetime', u'<0.523', u'0.542', u'0.583', u'0.626', u'0.673', u'0.723', u'0.777', u'0.835',
       u'0.898', u'0.965', u'1.037', u'1.114', u'1.197', u'1.286', u'1.382',
       u'1.486', u'1.596', u'1.715', u'1.843', u'1.981', u'10.37', u'11.14',
       u'11.97', u'12.86', u'13.82', u'14.86', u'15.96', u'17.15', u'18.43',
       u'19.81', u'2.129', u'2.288', u'2.458', u'2.642', u'2.839', u'3.051',
       u'3.278', u'3.523', u'3.786', u'4.068', u'4.371', u'4.698', u'5.048',
       u'5.425', u'5.829', u'6.264', u'6.732', u'7.234', u'7.774', u'8.354',
       u'8.977', u'9.647']

df_APS=df_APS[APS_cols]
df_APS['Total'] = df_APS.loc[:,u'0.542':u'9.647'].sum(axis=1)

df_APS.set_index('datetime', drop =True, inplace=True)

APS = df_APS['Hour'] 
SMPS = pd.read_pickle(picdir + 'smps.p')
df_SMPS =SMPS
df_SMPS['Total']=df_SMPS.loc[:,' 14.1':'736.5'].sum(axis=1)
df_SMPS.set_index('datetimes', drop =True, inplace =True)


fig, ax=plt.subplots()
final.set_index(final['3'], inplace =True)
final.index = pd.to_datetime(final.index)
ax=final.INP.plot(marker ='o', color ='b', alpha = 0.8)
ax.set_ylim(-2,2)

myFmt = mdates.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(myFmt)
majorLocator = MultipleLocator(4)
minorLocator = MultipleLocator(2)
ax.xaxis.set_major_locator(majorLocator)
ax.tick_params(axis='x',which='minor',bottom='on')


ax2=ax.twinx()
ax2=plt.plot(df_APS.Total.resample('0.5h').sum(), color='red')
plt.ylim(-100,10000)
plt.minorticks_on()
ax.xaxis.set_minor_locator(minorLocator)

#%%

APS_topiv = df_APS.Date.date


