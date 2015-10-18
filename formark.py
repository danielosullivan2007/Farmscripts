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

degree_sign= u'\N{DEGREE SIGN}'
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'





#Change directory to folder containing rates.csv file
indir='C:\\Users\\Daniel\\Documents\\farmscripts\\Stuff for mark\\'
rates = pd.read_csv(indir+'rates.csv')

rates1 = rates[rates['experiment']==1]

rates1['J+Tot']=rates1['J']+rates1['J+']
rates1['J-Tot']=rates1['J']-rates1['J-']

rates1['logJ']=rates1['J'].apply(np.log10)
rates1['logJ+']= rates1['J+Tot'].apply(np.log10)-rates1['logJ']
rates1['logJ-']=rates1['logJ']-rates1['J-Tot'].apply(np.log10)
yerr=(rates1['logJ+'], rates1['logJ-'])


rates3 = rates[rates['experiment']==3]

rates3['J+Tot']=rates3['J']+rates3['J+']
rates3['J-Tot']=rates3['J']-rates3['J-']

rates3['logJ']=rates3['J'].apply(np.log10)
rates3['logJ+']= rates3['J+Tot'].apply(np.log10)-rates3['logJ']
rates3['logJ-']=rates3['logJ']-rates3['J-Tot'].apply(np.log10)
yerr3=(rates3['logJ+'], rates3['logJ-'])


fig, ax1 = plt.subplots()
ax1.errorbar(x= rates3['T'], y=rates3['logJ'], xerr = 0.4, yerr=yerr3,fmt='o', 
             ecolor = 'b', lw=0.5, label = 'exp. 3' )
sns.regplot(x="T", y="logJ",  data=rates3, ax = ax1, color = 'b', ci= None)


ax1.errorbar(x= rates1['T'], y=rates1['logJ'], xerr = 0.4, yerr=yerr,fmt='o', ecolor = 'r',
             markerfacecolor = 'r', mec='r', lw=0.5, label = 'exp. 1')
sns.regplot(x="T", y="logJ",  data=rates1, ax = ax1, color = 'r', ci= None)
ax1.set_xlabel ('Temperature  ('+degree_sign+'C)')
ax1.set_ylabel(r'$\mathrm{Log_{10} \enspace  J \enspace (cm^{-2})}$' )
plt.legend()


