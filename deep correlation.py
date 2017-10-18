# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:10:58 2017

@author: useradmin
"""
import numpy as np
import pandas as pd
import seaborn as sns
picdir = 'C:\\Users\\useradmin\\Desktop\\Farmscripts\\Pickels\\'
#figdir =  
import os
import glob as glob
os.chdir(picdir)
to_import  = glob.glob('*data at minus*.csv')
names = ['Temp','Unnamed: 0',
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
 'APS Total',
 'SMPS Total',
 '3',
 'demott']


df = pd.DataFrame(columns = names)


for i in range(len(to_import)):
    x = pd.read_csv(to_import[i])
    x['Temp']=-1*float(to_import[i][13:15])
    join =   [df, x]
    df = pd.concat(join).drop('Unnamed: 0', axis =1)

df = df[['3','Temp', 'INP',
         '10cm Soil Temperature',
 'APS Total',
 'Concrete Temperature',
 'Dew Point Temperature',
 'Dry Bulb Temperature',
 'Grass Temperature',
 'Humidity',
 'MAX_GUST_CTIME',
 'MAX_GUST_DIR',
 'MAX_GUST_SPEED',
 'MEAN_WIND_SPEED',
 'Radiation Total since 0900',
 'Rainfall Total since 0900',
 'SMPS Total',
 'demott']].rename(columns ={'3':'Date'})


df.drop( ['MAX_GUST_CTIME','MAX_GUST_DIR', 'demott','10cm Soil Temperature'])
df_15 = df[df['Temp']==-20]
df_apstrim = df_15[df_15['APS Total']<10000]
df_apstrim.reset_index(drop = True, inplace =True)
df_apstrim['log_APS'] = df_apstrim['APS Total'].apply(np.log10)
sns.pairplot(data =df_apstrim, y_vars=['INP'],
             x_vars= ['Humidity','Dry Bulb Temperature' ,'MEAN_WIND_SPEED','Rainfall Total since 0900'])   
sns.pairplot(data =df_apstrim, y_vars=['INP'],
             x_vars= ['SMPS Total','log_APS'])   
#sns.residplot('INP', 'log_APS', data =df_apstrim)