# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 16:55:22 2018

@author: Daniel
"""
import pandas as pd
import seaborn as sns
import os as os
import matplotlib.pyplot as plt
import numpy as np


#Change directory to folder containing rates.csv file
indir='C:\\Users\\Daniel\\Documents\\farmscripts\\Stuff for mark\\'
rates = pd.read_csv(indir+'rates.csv')

rates['J+Tot']=rates['J']+rates['J+']
rates['J-Tot']=rates['J']-rates['J-']

rates['logJ']=rates['J'].apply(np.log10)
rates['logJ+']= rates['J+Tot'].apply(np.log10)-rates['logJ']
rates['logJ-']=rates['logJ']-rates['J-Tot'].apply(np.log10)
yerr=(rates['logJ+'], rates['logJ-'])


fig, ax1 = plt.subplots()
ax1.errorbar(x= rates['T'], y=rates['logJ'], yerr=yerr,fmt='o', ecolor = 'r')
sns.regplot(x="T", y="logJ",  data=rates, ax = ax1)



