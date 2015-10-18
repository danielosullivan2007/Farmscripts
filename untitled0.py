# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:20:17 2018

@author: Daniel
"""

import pandas as pd
import glob

a = 'C:\\Users\\Daniel\\Desktop\\join\\'

x=glob.glob(a+'*.csv')
df = pd.DataFrame()

for i in range (len(x)):
    if i ==0:
        df = pd.read_csv(x[i])
    else: 
        z= pd.read_csv(x[i])
        z.rename(columns ={'blah':'REPORTING_PERIOD'}, inplace = True)
        
        df =df.append(z)

df['REPORTING_PERIOD'] = pd.to_datetime(df['REPORTING_PERIOD'], format  = '%b-%y')    
df.reset_index(inplace =True)