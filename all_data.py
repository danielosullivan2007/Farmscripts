# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 10:11:29 2017

@author: eardo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from directories import farmdirs


data=pd.read_csv(farmdirs['pickels']+'non_binned_data_all.csv')
data.drop(['Unnamed: 0','K'], axis =1, inplace =True)
data.drop([0,1], axis =0, inplace =True)
data['start']=pd.to_datetime(data['start'])
data['end']=pd.to_datetime(data['end'])
data.reset_index(drop =True, inplace =True)
data.set_index('start', inplace = True)


#T=-24
#data  = data[(data['T']>T-1) & (data['T']<T+1)]
#data  = data[(data['T']>T-1) & (data['T']<T+1)]

data = data.loc['2016-10-5':'2016-10-8']


fig, ax=plt.subplots()
ax.plot(data['T'], data['INPs_perL'], lw=0, marker='o')
ax.set_yscale('log')