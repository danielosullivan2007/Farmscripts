# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:22:25 2017

@author: eardo
"""
import os 
import pandas as pd
from datetime import datetime
os.chdir('C:\\Users\\eardo\\Desktop\\Farmscripts\\')
from myfuncs import num2words
import seaborn as sns


df=pd.read_csv('observations.csv')
picdir = 'C:\\Users\\eardo\\Desktop\\Farmscripts\\Pickels\\'

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
    
minus15=data[-25]   
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
sns.tsplot(final.INP[final.Agri_Tractor==1], interpolate=False, condition='Acitivy', color='r')
sns.tsplot(final.INP[final.Agri_Tractor==0], interpolate=False, condition='no Acitivy')

#sns.tsplot(final.INP[final.Agri_Tractor==1], interpolate=False, condition='Acitivy')







