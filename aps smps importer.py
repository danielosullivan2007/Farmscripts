# -*- coding: utf-8 -*-
"""
Created on Thu May 04 14:56:19 2017

@author: eardo
"""

import os 
import numpy as np
import pandas as pd
import glob
import datetime


indir = ('W:\APS')

os.chdir(indir)

#==============================================================================
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

#aps=pd.read_pickle(indir+"aps.p")

indir = ('W:\SMPS')

os.chdir(indir)
df_smps = pd.DataFrame()
a=glob.glob('*.csv')

for i in range(len(a)):
    df=pd.read_csv(a[i], delimiter =',', header =25, skip_footer=30)
    df=df.drop(df.index[2:8])

    
    df = df.transpose()
    
    df.columns = df.iloc[0][:]
    df=df.drop(df.index[0])
    df['datetime']=pd.to_datetime(df['Date']+" "+df['Start Time'])
    df=df.drop(['Date', 'Start Time'], axis =1)
    
    df_smps = df_smps.append(df, ignore_index=True)
datetimes = df_smps['datetime']
df_smps.drop('datetime', axis =1, inplace = True)
df_smps = df_smps.iloc[:,1:].astype(float)
df_smps.insert(0,'datetimes', datetimes)
   # df_smps.iloc[0:, 1:] = df_smps.iloc[0:, 1:].astype(float)
df_smps.to_pickle('C:\Users\eardo\Desktop\Farmscripts\Pickels\smps.p')
