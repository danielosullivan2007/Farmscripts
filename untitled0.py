# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 12:17:55 2017

@author: eardo
"""

import pandas as pd
import matplotlib.pyplot as plt
from directories import farmdirs
import numpy as np


data = pd.read_csv(farmdirs['pickels']+'all_data_with_met.csv')
data.reset_index(inplace=True)
data['INP']= 10**data['INP']
data['APS Total ']= data['APS Total'].apply(np.log10)
data_24 = data[data['Temp']==-24]
data_23 = data[data['Temp']==-23]
data_22 = data[data['Temp']==-22]
data_21 = data[data['Temp']==-21]
data_20 = data[data['Temp']==-20]
data_19 = data[data['Temp']==-19]
data_18 = data[data['Temp']==-18]
data_17 = data[data['Temp']==-17]
data_16 = data[data['Temp']==-16]

import seaborn as sns


f, ax = plt.subplots(figsize=(7, 7))
#ax.set(xscale="log", yscale="log")
sns.jointplot(x='APS Total', y = 'INP',data =data_24)
#plt.xlim(100,1000000)
#plt.xscale('log')
#plt.yscale('log')


