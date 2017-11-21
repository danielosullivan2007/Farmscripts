# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:28:14 2017

@author: eardo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

degree_sign= u'\N{DEGREE SIGN}'

db = 'T:\\'
# =============================================================================
# xl = pd.ExcelFile('C:\\Users\\eardo\\Desktop\\feldspar.xlsx')
# sheets = xl.sheet_names  # see all sheet names
# test = xl.parse(sheets[2])  # read a specific sheet to DataFrame
# =============================================================================

df = pd.read_excel(db+'K-Feldspar.xlsx', sheetname = "Sheet1")
atk13 = pd.read_excel(db+'K-Feldspar.xlsx', sheetname = "Sheet3")
codes= pd.read_excel(db+'K-Feldspar.xlsx', sheetname = "Codes")

codes = dict(zip(codes['Abb'], codes['Source']))

clean_dict= dict(zip('n/d', [np.nan]))
df['wt_pc'].replace(to_replace = 'n/d',value =np.nan,  inplace =True)

bins =  [ 0.0009, 0.0099, 0.05, 0.1, 1]
names=['0.001', '0.01', '0.1', '0.5-1']
df['conc'] = pd.cut(df['wt_pc'], bins =bins, labels=names)
cols = [u'T', u'ns', u'wt_pc','conc', u'V_drop', u'r_drop', u'experiment', u'Ref' ]
df = df[cols]



a= df[df['conc']=='0.5-1']
b= df[df['conc']=='0.1']
c= df[df['conc']=='0.01']
d= df[df['conc']=='0.001']


fig, ax = plt.subplots()
ax.scatter(a['T'], a['ns'], color ='c', label = '0.5-1' )
ax.scatter(b['T'], b['ns'], color ='r', label = '0.1', zorder =20)
ax.scatter(c['T'], c['ns'], color = 'g', label ='0.01')
ax.scatter(d['T'], d['ns'], color ='b', label = '0.001')
ax.plot(atk13['T'], atk13['ns'], color = 'k', label ='Atk.13', linewidth =5)
plt.legend(scatterpoints =1)

plt.yscale('log')
plt.xlabel('T ('+degree_sign+'C)')
plt.ylabel('n$_s$ cm$^{-2}$')