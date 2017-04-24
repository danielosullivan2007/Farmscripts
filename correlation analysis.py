# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:02:47 2017

@author: Daniel
"""

import pandas as pd
import numpy as np
import os

indir = '/Users/Daniel/Desktop/farmscripts/MetData/Wind'
os.chdir(indir)

#==============================================================================
# wind= pd.read_csv('wind.csv', delimiter = ',')
# met=pd.read_csv('Metall.csv',delimiter =',')
# 
# INPs=pd.read_csv('INPs copy.csv', delimiter =',' ).dropna(axis=0, how = 'any')
# INPs.reset_index(inplace=True, drop =True)
# INPs.reindex(index=range(len(INPs['end'])))
# INPs.rename(columns={'Date': 'Datetime'}, inplace = True)
# INPs.drop('Unnamed: 0', axis = 1, inplace=True)
# INPs['Datetime']=INPs['Datetime'].astype(str)
# 
# INPs['Date']=INPs.Datetime.str[0:6]
# INPs['Date']=INPs.Date.str[4:6]+"-"+INPs.Date.str[2:4]+"-"+INPs.Date.str[0:2]
# 
# 
# met['Time']=met['Time'].astype(str)
# INPs['end']=INPs['end'].astype(str)
# #==============================================================================
# # for i in range(len(INPs.end)):
# #     INPs.end[i]=INPs.end[i][0:2]+':'+ INPs.end[i][2:4]
# #==============================================================================
#     
# INPs['Datetime'] = pd.to_datetime(INPs['Date']+ " " + INPs['end'], dayfirst=True)
# for i in range(len(met.Time)):
#     if met['Time'][i]=='0':
#         met['Time'][i]='0000'
#     elif len(met['Time'][i])==3:
#         met['Time'][i]='0'+met['Time'][i]
# 
# for i in range(len(met.Time)):
#     met['Time'][i]=met['Time'][i][0:2]+':'+met['Time'][i][2:4]
# 
# for i in range(len(met['Date'])):
#     met['Date'][i]=met['Date'][i].replace("/","-")
#     if len(met['Date'][i])==8:
#         met['Date'][i]="0"+met['Date'][i]
#     
# 
# met['Datetime']=pd.to_datetime(met['Date']+" "+ met['Time'], dayfirst = True)     
# met.set_index('Datetime', inplace = True)
# 
# 
# wind.set_index('OB_END_TIME',  inplace=True)
# wind.index=pd.to_datetime(wind.index, dayfirst = True)
# 
# 
# df15 = INPs.loc[INPs['T'] ==-15]
# 
# #average duplicate values
# df15=df15.groupby('Datetime',as_index=False).mean()
# df15 = df15.set_index("Datetime", drop = True)
# 
# test = wind.reindex(df15.index, method = 'nearest')
# result=pd.concat([df15, test], axis =1)
# 
# met2= met.reindex(df15.index, method ='nearest')
#==============================================================================

SMPS= pd.read_csv('SMPS.csv', delimiter = ',')
SMPS.Time=SMPS.Time.astype(str)
SMPS.Date=SMPS.Date.astype(str)

for i in range(len(SMPS['Time'])):
    SMPS['Time'][i]=SMPS['Time'][i][0:2]+':'+SMPS['Time'][i][2:4]

for i in range(len(SMPS['Date'])):
    SMPS['Date'][i]=SMPS['Date'][i][4:6]+"-"+SMPS['Date'][i][2:4]+"-"+SMPS['Date'][i][0:2]

SMPS['Datetime']=pd.to_datetime(SMPS['Date']+" "+ SMPS['Time'], dayfirst = True)     
SMPS.set_index('Datetime', inplace = True)

SMPS.sort_index(inplace = True)
#==============================================================================
# SMPS2= SMPS.reindex(df15.index, method ='nearest')
# result = pd.concat([result, SMPS2], axis =1)
#==============================================================================
